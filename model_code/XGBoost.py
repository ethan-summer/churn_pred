import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

def log_loss_with_penalties(preds, dtrain):  
    epsilon = 1 #避免对0做log操作
    labels = dtrain.get_label()  # 获取真实标签值
    penalty_coefficient_type1 = 1.0  
    penalty_coefficient_type2 = 0.1  
    # 这两个变量作为一个惩罚项的系数，这里定义了二分类中，类别1和类别2的错误分类分别拥有不同的惩罚系数。

    log_loss = np.sum(-labels * np.log(preds + epsilon) - (1 - labels) * np.log(1 - preds + epsilon))
    # 这是标准的 log loss，标准的 log loss 衡量了预测值与真实标签值之间的差距。
    penalty_term_type1 = penalty_coefficient_type1 * np.sum((1 - labels) * (preds ** 2))  
    penalty_term_type2 = penalty_coefficient_type2 * np.sum(labels * ((1 - preds) ** 2))  

    # 下面两行计算损失函数关于预测值的一阶导数和二阶导数，也就是梯度和海森矩阵。
    grad = -labels / preds + (1 - labels) / (1 - preds) + 2 * penalty_coefficient_type1 * (1 - labels) * preds - 2 * penalty_coefficient_type2 * labels * (1 - preds)  
    hess = 1 / preds ** 2 + 1 / (1 - preds) ** 2 + 2 * penalty_coefficient_type1 * (1 - labels) - 2 * penalty_coefficient_type2 * labels  

    return grad, hess  # 返回梯度和海森矩阵，XGBoost会利用这些信息进行下一步的优化。 

# 自定义评估函数输出自定义的损失值
def custom_eval_metric(preds, dtrain): 
    epsilon = 1
    labels = dtrain.get_label()
    penalty_coefficient_type1 = 1.0  
    penalty_coefficient_type2 = 0.1  
    log_loss = np.sum(-labels * np.log(preds + epsilon) - (1 - labels) * np.log(1 - preds + epsilon))
    penalty_term_type1 = penalty_coefficient_type1 * np.sum((1 - labels) * (preds ** 2))  
    penalty_term_type2 = penalty_coefficient_type2 * np.sum(labels * ((1 - preds) ** 2))  
    total_loss = log_loss + penalty_term_type1 + penalty_term_type2
    return 'custom_loss', total_loss


def xgboost(file_path):
    df = pd.read_csv(file_path, encoding="gbk")  
    df=df.fillna(0)  
    X = df.iloc[:, :-1] 
    y = df.iloc[:, -1]  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  
    
    # 将训练集和测试集转化为xgboost所需的DMatrix格式
    dtrain = xgb.DMatrix(X_train, label=y_train)  
    dtest = xgb.DMatrix(X_test, label=y_test)  
    
    # 设置XGBoost参数  
    param = {}  
    
    # 使用XGBoost的train函数进行模型训练，定义了模型参数，训练轮数，优化的损失函数和评估函数以及早停等参数。
    num_round = 100  
    evals_result = {}  
    evals = [(dtrain, 'train'), (dtest, 'test')]  
    bst = xgb.train(param, dtrain, num_round, obj=log_loss_with_penalties, evals=evals, feval=custom_eval_metric, evals_result=evals_result, verbose_eval=True, early_stopping_rounds=10)
    
    # 使用训练好的模型进行预测   
    preds = bst.predict(dtest)

    # 将预测结果转换为0和1的标签  
    y_pred_labels = [1 if pred >= 0.5 else 0 for pred in preds]
    
    return y_pred_labels, y_test, preds
    

# # 计算准确率  
# accuracy = accuracy_score(y_test, preds)
# print("Test Accuracy: {:.2f}%".format(accuracy * 100))

# # 计算F1-score
# f1 = f1_score(y_test, preds)
# print("F1 score: {:.2f}".format(f1))

# # 画出ROC曲线
# fpr, tpr, thresholds = roc_curve(y_test, preds)
# roc_auc = roc_auc_score(y_test, preds)
# plt.figure()
# plt.plot(fpr, tpr, color='darkorange', label='ROC curve (area = %0.2f)' % roc_auc)
# plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver Operating Characteristic')
# plt.legend(loc="lower right")
# plt.show()

# # 打印混淆矩阵
# cm = confusion_matrix(y_test, preds)
# print('Confusion Matrix: n', cm)

# # 输出模型训练过程中的损失值情况  
# print("Evaluation results:")
# for key in sorted(evals_result.keys()):
#     print("%s: %f" % (key, evals_result[key]['custom_loss'][-1]))
