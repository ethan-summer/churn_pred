# -*- coding:UTF-8 -*-
from matplotlib.font_manager import FontProperties
from sklearn.metrics import f1_score
from smote import preprocess_data , preprocess_tset_data
from DES import encrypt_csv_column , decrypt_csv_column
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import argparse

def sigmoid(x):
    threshold = 20.0
    inX_clipped = np.clip(x, -threshold, threshold)
    return 1.0 / (1.0 + np.exp(-inX_clipped))

def stocGradAscent1(train_file_path, batchSize=32, numIter=200, lambda_reg=0.01):
    x_train, y_train, x_test, y_test = preprocess_data(file_path=train_file_path)
    m, n = np.shape(x_train)
    weights = np.ones(n)   # 初始化权重，确保是n维的
    weights_array = np.array([])
    eps = 1e-6  # 避免除零错误的小值

    for j in range(numIter):
        dataIndex = list(range(m))
        np.random.shuffle(dataIndex) 
        for k in range(0, m, batchSize):
            batchIndex = dataIndex[k:min(k + batchSize, m)]  
            dataBatch = x_train[batchIndex]
            labelBatch = y_train[batchIndex]
            h = sigmoid(np.dot(dataBatch, weights))  
            error = labelBatch - h  
            gradient = np.dot(error, dataBatch) / batchSize  # 计算梯度，取小批量样本的平均值
            alpha = 4 / (1.0 + j + k) + 0.01  # 降低alpha的大小，每次迭代减小
            weights = weights + alpha * (gradient - lambda_reg * weights) / (
                np.sqrt(np.sum(np.square(gradient))) + eps)  # 更新回归系数，添加L2正则化项和AdaGrad算法
            weights_array = np.append(
                weights_array, weights, axis=0)  # 添加回归系数到数组中
    weights_array = weights_array.reshape(
        numIter * ((m + batchSize - 1) // batchSize), n)  # 改变维度
    np.save('trainWeights_0.2.npy', weights)
    return weights, weights_array

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0

def colicTest(train_file_path):
    _, _, x_test, y_test = preprocess_data(train_file_path)
    trainWeights = np.load('./prediction_service/model/training_weights/trainWeights_0.2.npy')
    predictions = []
    predicted_score = []
    print(x_test.shape)
    for i in range(len(x_test)):
        predicted_label = int(classifyVector(np.array(x_test[i]), trainWeights))
        #仅仅获得概率不转化成0或者1
        score =   sigmoid(np.dot(x_test[i], trainWeights))
        predictions.append(predicted_label)
        predicted_score.append(score)
        
    return predictions, y_test, predicted_score


    
def Test_write_back(test_file_path,key):#
    trainWeights = np.load('prediction_service/model/training_weights/trainWeights_0.2.npy')
    
    test_data = pd.read_csv(test_file_path, engine="python", encoding="gbk")
    x_test = test_data.fillna(0).values[:, 1:]
    

    scaler = StandardScaler()
    x_test = scaler.fit_transform(x_test)
    

    predictions = []
    for i in range(len(x_test)):
        predicted_label = int(classifyVector(np.array(x_test[i]), trainWeights))
        predictions.append(predicted_label)

    test_data['pred_result'] = predictions
    #新文件名原来的路径结尾加上encrypt
    new_file_path = test_file_path.split(".")[0] + "_encrypt.csv"
    test_data.to_csv(new_file_path, index=False, encoding="gbk")
    encrypt_csv_column(new_file_path,key)

def decrypt_data(test_file_path,key):
    
    test_data = pd.read_csv(test_file_path, engine="python", encoding="gbk")
    new_file_path = test_file_path.split(".")[0] + "_to_decrypt.csv"
    test_data.to_csv(new_file_path, index=False, encoding="gbk")
    
    decrypt_csv_column(new_file_path,key)

if __name__ == '__main__':
    argsparser = argparse.ArgumentParser()
    
    argsparser.add_argument('--train_file_path', type=str, default='prediction_service\model\input\internet_service_churn.csv',
                        help='Training set path')
    argsparser.add_argument('--test_file_path', type=str, default='prediction_service\model\input_test\churn_test.csv',
                        help='Testing set path')
    argsparser.add_argument('--encrypt_file_path', type=str, default='prediction_service\model\input_test\churn_test_encrypt.csv',
                        help='Testing set path')
    argsparser.add_argument(
        "--encrypt_data",
        "-ed",
        action="store_true",
        help="encrypt data"
    )
    argsparser.add_argument(
        "--decrypt_data",
        "-dd",
        action="store_true",
        help="decode data file",
    )
    
    args = argsparser.parse_args()
        
    stocGradAscent1(args.train_file_path)

