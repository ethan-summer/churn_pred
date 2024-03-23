import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, f1_score,roc_curve, auc
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.feature_selection import SelectFromModel
from sklearn.cluster import KMeans
import warnings


def random_forest(file_path):

    warnings.filterwarnings("ignore", category=UserWarning)

    # 读取CSV文件
    data = pd.read_csv(file_path, encoding="gbk")  
    data = data.fillna(0)

    # 分离特征和标签
    X = data.iloc[:, 1:-1]
    y = data.iloc[:, -1]

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # 初始化随机森林模型
    rf = RandomForestClassifier(n_estimators=100, random_state=42)

    # 训练随机森林
    rf.fit(X_train, y_train)

    # 计算每棵树的AUC值
    trees = rf.estimators_
    auc_scores = [roc_auc_score(y_train, tree.predict_proba(X_train)[:, 1]) for tree in trees]

    # 定义一个阈值范围
    thresholds = np.linspace(0.5, 0.9, 20)  # 例如，从0.5到0.9，共20个不同的阈值

    # 初始化交叉验证折数
    cv = StratifiedKFold(n_splits=5)

    # 用于存储每个阈值的性能
    performance = []

    # 遍历所有阈值
    for threshold in thresholds:
        auc_scores = []  # 初始化auc_scores列表
        f1_scores = []  # 初始化f1_scores列表
        for train_index, val_index in cv.split(X_train, y_train):
            X_train_fold, X_val_fold = X_train.iloc[train_index], X_train.iloc[val_index]
            y_train_fold, y_val_fold = y_train.iloc[train_index], y_train.iloc[val_index]

            # 计算当前折叠的AUC分数
            y_proba = np.mean([tree.predict_proba(X_val_fold)[:, 1] for tree in trees], axis=0)
            fpr, tpr, _ = roc_curve(y_val_fold, y_proba)
            auc_score = auc(fpr, tpr)
            
            # 筛选出AUC值超过阈值的决策树
            selected_trees_fold = [tree for tree, proba in zip(trees, y_proba) if proba.max() > threshold]
            
            # 计算加权性能
            y_proba_avg = np.mean([tree.predict_proba(X_val_fold)[:, 1] for tree in selected_trees_fold], axis=0)
            
            #将预测概率转换为二进制分类结果（这里使用0.5作为阈值）
            y_pred_fold = (y_proba_avg >= 0.5).astype(int)
            
            auc_scores.append(roc_auc_score(y_val_fold, y_proba_avg))

            # 计算当前折叠的F1分数
            f1= f1_score(y_val_fold, y_pred_fold, average='binary')
            f1_scores.append(f1)
        
        # 计算加权性能的平均值
        weighted_auc = np.mean(auc_scores) if auc_scores else 0
        weighted_f1 = np.mean(f1_scores) if f1_scores else 0
        performance.append((weighted_auc, weighted_f1))

    # 选择最佳阈值
    best_threshold = thresholds[np.argmax([auc + f1 for auc, f1 in performance])]


    # 使用最佳阈值重新筛选决策树
    selected_trees = [tree for tree, auc_score in zip(trees, auc_scores) if auc_score > best_threshold]

    # 对筛选出的决策树进行聚类
    kmeans = KMeans(n_clusters=3, random_state=42)  # 假设我们选择3个聚类中心
    tree_features = np.array([selected_tree.feature_importances_ for selected_tree in selected_trees])
    kmeans.fit(tree_features.reshape(-1, 1))

    # 获取聚类中心对应的决策树索引
    centroids = kmeans.cluster_centers_
    tree_indices = centroids.astype(int)

    # 选择聚类中心对应的决策树
    centroid_trees = [selected_trees[int(index)] for index in tree_indices]

    # 创建一个新的RandomForestClassifier实例并使用fit方法来训练模型
    improved_rf = RandomForestClassifier(n_estimators=len(centroid_trees), random_state=42)
    improved_rf.fit(X_train, y_train)

    # 使用改进的随机森林模型进行预测
    y_pred_proba = improved_rf.predict_proba(X_test)[:, 1]
    y_pred_labels = (y_pred_proba >= 0.5).astype(int)
    return y_pred_labels, y_test, y_pred_proba






    

