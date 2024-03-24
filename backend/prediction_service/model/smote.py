import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np


def preprocess_data(file_path,  test_size=0.15, random_state=42):
    # 从Excel文件中导入数据集
    data = pd.read_csv(file_path, engine="python", encoding="gbk")
    data = data.fillna(0)

    x = data.iloc[:, 1:-1].values 
    print(x.shape)
    y = data.iloc[:, -1].values  

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state)

    # 标准化特征数据
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 初始化SMOTE对象
    smote = SMOTE(random_state=random_state)

    # 对训练集应用SMOTE算法进行均衡化处理
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

    # 转换为NumPy格式
    X_train_res = np.array(X_train_res)
    X_test = np.array(X_test)
    y_train_res = np.array(y_train_res)
    y_test = np.array(y_test)

    return X_train_res, y_train_res, X_test, y_test

def preprocess_tset_data(file_path):
    data = pd.read_csv(file_path, engine="python", encoding="gbk")
    
    data = data.fillna(0)
    
    x = data.iloc[:, :-1].values 
    y = data.iloc[:, -1].values
    
    scaler = StandardScaler()
    x_std = scaler.fit_transform(x)
    
    
    x_process = np.array(x_std)
    y_process = np.array(y)
    return x_process, y_process
    