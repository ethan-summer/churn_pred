import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import warnings
from logic import colicTest,Test_write_back, decrypt_data
from random_forest import random_forest , random_forest_pred_and_encrypt
from XGBoost import xgboost,xgboost_pred_and_encrypt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


def model_performance(file_path):

    model_names = ['LogisticRegression', 'RandomForest', 'XGBoost']
    
    pred1,label1,preds1 = colicTest(file_path)
    pred2,label2,preds2 = random_forest(file_path)
    pred3,label3,preds3 = xgboost(file_path)

    # 准确率
    accuracy1 = accuracy_score(label1, pred1)
    accuracy2 = accuracy_score(label2, pred2)
    accuracy3 = accuracy_score(label3, pred3)

    for i, (pred, label) in enumerate([(pred1, label1), (pred2, label2), (pred3, label3)]):
    # 计算准确率
        accuracy = accuracy_score(label, pred)
        
        # 绘制条形图
        plt.figure(figsize=(6, 4))
        plt.bar([model_names[i]], [accuracy],width=0.01)
        plt.xlabel('Model')
        plt.ylabel('Accuracy')
        plt.title(f'{model_names[i]} Accuracy')

        # 保存单个模型的图片
        plt.savefig(f'./prediction_service/model/model_performance_output/accuracy_{model_names[i]}.png')
        plt.clf()


    plt.figure()  # 创建新的图形
    plt.bar(['LogisticRegression','RandomForest','XGBoost'],[accuracy1,accuracy2,accuracy3])
    plt.xlabel('Model')
    plt.ylabel('Accuracy')
    plt.title('Model Accuracy')
    plt.savefig('./prediction_service/model/model_performance_output/accuracy.png')
    
    # 混淆矩阵
    confusion_matrix1 = confusion_matrix(label1, pred1)
    confusion_matrix2 = confusion_matrix(label2, pred2)
    confusion_matrix3 = confusion_matrix(label3, pred3)

    plt.figure(figsize=(10, 15))  # 增大图的高度

    plt.subplot(3, 1, 1)
    sn.heatmap(confusion_matrix1, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.title('Confusion Matrix of LogisticRegression')

    plt.subplot(3, 1, 2)
    sn.heatmap(confusion_matrix2, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.title('Confusion Matrix of RandomForest')

    plt.subplot(3, 1, 3)
    sn.heatmap(confusion_matrix3, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.title('Confusion Matrix of XGBoost')

    plt.subplots_adjust(hspace=0.5)  # 增大垂直间距
    plt.savefig('./prediction_service/model/model_performance_output/confusion_matrix.png')
    
    
    for i, (confusion_matrix_, model_name) in enumerate([(confusion_matrix1, model_names[0]), (confusion_matrix2, model_names[1]), (confusion_matrix3, model_names[2])]):
        plt.figure(figsize=(8, 6))
        sn.heatmap(confusion_matrix_, annot=True, fmt='d', cmap='Blues')
        plt.xlabel('Predicted label')
        plt.ylabel('True label')
        plt.title(f'Confusion Matrix of {model_name}')
        plt.savefig(f'./prediction_service/model/model_performance_output/confusion_matrix_{model_name}.png')
        plt.clf()
        
    # ROC曲线
    fpr1, tpr1, thresholds1 = roc_curve(label1, preds1)
    fpr2, tpr2, thresholds2 = roc_curve(label2, preds2)
    fpr3, tpr3, thresholds3 = roc_curve(label3, preds3)
    
    roc_auc1 = roc_auc_score(label1, preds1)
    roc_auc2 = roc_auc_score(label2, preds2)
    roc_auc3 = roc_auc_score(label3, preds3)

    plt.figure(figsize=(10, 8))
    plt.plot(fpr1, tpr1, color='red', lw=2, label='Model 1 ROC curve (area = %0.2f)' % roc_auc1)
    plt.plot(fpr2, tpr2, color='green', lw=2, label='Model 2 ROC curve (area = %0.2f)' % roc_auc2)
    plt.plot(fpr3, tpr3, color='blue', lw=2, label='Model 3 ROC curve (area = %0.2f)' % roc_auc3)
    plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic comparison')
    plt.legend(loc="lower right")
    plt.savefig('./prediction_service/model/model_performance_output/combined_roc.png')
    
    for i, (fpr, tpr, roc_auc, model_name) in enumerate([(fpr1, tpr1, roc_auc1, model_names[0]), (fpr2, tpr2, roc_auc2, model_names[1]), (fpr3, tpr3, roc_auc3, model_names[2])]):
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='red', lw=2)
        plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'{model_name} ROC Curve (AUC = {roc_auc:.2f})')
        plt.legend(['ROC curve'], loc="lower right")
        plt.savefig(f'./prediction_service/model/model_performance_output/roc_{model_name}.png')
        plt.clf()
    
    
    
    #PR曲线
    precision1, recall1, _ = metrics.precision_recall_curve(label1, preds1)
    precision2, recall2, _ = metrics.precision_recall_curve(label2, preds2)
    precision3, recall3, _ = metrics.precision_recall_curve(label3, preds3)

    plt.figure()  # 创建新的图形
    plt.plot(recall1, precision1, label='Model 1 - ColicTest')
    plt.plot(recall2, precision2, label='Model 2 - Random Forest')
    plt.plot(recall3, precision3, label='Model 3 - XGBoost')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.legend()
    plt.title('Precision-Recall Curves')
    plt.savefig('./prediction_service/model/model_performance_output/precision_recall.png')
    
    
    for i, (precision, recall, model_name) in enumerate([(precision1, recall1, model_names[0]), (precision2, recall2, model_names[1]), (precision3, recall3, model_names[2])]):
        plt.figure(figsize=(8, 6))
        plt.plot(recall, precision, lw=2)
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title(f'{model_name} Precision-Recall Curve')
        plt.savefig(f'./prediction_service/model/model_performance_output/precision_recall_{model_name}.png')
        plt.clf()
    
    
    # F1值
    f1 = f1_score(label1, pred1)
    f2 = f1_score(label2, pred2)
    f3 = f1_score(label3, pred3)

    plt.figure()  # 创建新的图形
    plt.bar(['LogisticRegression','RandomForest','XGBoost'],[f1,f2,f3])
    plt.xlabel('Model')
    plt.ylabel('F1')
    plt.title('Model F1')
    plt.savefig('./prediction_service/model/model_performance_output/f1.png')
    
    
    for i, (f, model_name) in enumerate([(f1, model_names[0]), (f2, model_names[1]), (f3, model_names[2])]):
        plt.figure(figsize=(8, 6))
        plt.bar(model_name, f,width=0.01)
        plt.xlabel('Model')
        plt.ylabel('F1')
        plt.title(f'{model_name} F1 Score')
        plt.savefig(f'./prediction_service/model/model_performance_output/f1_{model_name}.png')
        plt.clf()  
    

def register_filepath_command(
    subparsers: argparse._SubParsersAction,
) -> None:
    parser = subparsers.add_parser("model_performance", help="Your command description here")
    parser.add_argument(
        '--train_file_path', 
        type=str, 
        default='/home/xyj/Downloads/code/1/input/internet_service_churn.csv',
        help='Training set path')

def register_encrypt_command(
    subparsers: argparse._SubParsersAction,
) -> None:
    parser = subparsers.add_parser("train", help="Your command description here")
    parser.add_argument(
        '--test_file_path', 
        type=str, 
        default='/home/xyj/Downloads/code/1/input_test/churn_test.csv',
        help='Testing set path')

    

if __name__ == "__main__":

    argsparser = argparse.ArgumentParser()
    
    argsparser.add_argument('--train_file_path', type=str, default='prediction_service\model\input\internet_service_churn.csv',
                        help='Training set path')
    argsparser.add_argument('--test_file_path', type=str, default='prediction_service\model\input_test\churn_test.csv',
                        help='Testing set path')
    argsparser.add_argument('--encrypt_file_path', type=str, default='prediction_service\model\input_test\churn_test_encrypt.csv',
                        help='Encrypt file path set path')
    argsparser.add_argument('--model',type=str,default='LogisticRegression',help='model name')
    
    argsparser.add_argument(
        "--key",
        type=str,
        default="churnkey",
        help="key for encrypt and decrypt"
    )
    argsparser.add_argument(
        "--encrypt_data",
        "-ed",
        action="store_true",
        help="encrypt"
    )
    argsparser.add_argument(
        "--decrypt_data",
        "-dd",
        action="store_true",
        help="decrypt",
    )
    args = argsparser.parse_args()
    key = args.key.encode('ascii') 
    if args.encrypt_data:
        if args.model == 'xgboost':
            xgboost_pred_and_encrypt(args.test_file_path,key)
            exit()
        if args.model == 'random_forest':
            random_forest_pred_and_encrypt(args.train_file_path, args.test_file_path,key)
            exit()
        else:    
            Test_write_back(args.test_file_path, key)
            exit()

    if args.decrypt_data:
        decrypt_data(args.encrypt_file_path,key)
        exit()
    #训练文件目录train_file_path  输出文件
    model_performance(args.train_file_path)
    