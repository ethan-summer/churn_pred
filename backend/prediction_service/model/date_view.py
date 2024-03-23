import numpy as np
import sklearn as sk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.datasets import load_digits
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import seaborn as sn
import matplotlib.pyplot as plt
#from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report

plt.rcParams['font.sans-serif']=['SimHei']##中文乱码问题！
plt.rcParams['axes.unicode_minus']=False#横坐标负号显示问题！

data=pd.read_csv("input/internet_service_churn.csv",engine="python",encoding="gbk")

#客户流失情况
data_label = data.groupby("churn").size()
datas = list(zip(data_label.index.to_list(), data_label.to_list()))
datas = np.array(datas)
plt.pie(datas[:, 1], labels=datas[:, 0], autopct="%.1f%%") 
plt.legend(datas[:, 0], loc="upper left")
plt.title("客户流失情况分析") 
plt.show()

#近三月账单平均值情况直方图
plt.hist(x = data.bill_avg,
         bins = 80, # 指定直方图中条块的个数
         color = 'steelblue')
plt.xlabel('账单水平')
plt.ylabel('频数')
plt.title('近三个月账单平均值分布情况')
plt.show()

#是否订阅电视频道与客户流失的关系直方图
ax = plt.subplots(figsize=(5, 4))
count1 = len(data[(data["是否订阅电视频道"] == 0 ) & (data["churn"] == 0 )])
count2 = len(data[(data["是否订阅电视频道"] == 0 ) & (data["churn"] == 1 )])
count3 = len(data[(data["是否订阅电视频道"] == 1 ) & (data["churn"] == 0 )])
count4 = len(data[(data["是否订阅电视频道"] == 1 ) & (data["churn"] == 1 )])

x=['订阅电视频道','未订阅电视频道']
y1=[count1,count3]
y2=[count2,count4]

bar_width = 0.3
index_y1 = np.arange(len(x)) # 流失条形图的横坐标
index_y2 = index_y1 + bar_width # 未流失条形图的横坐标
plt.bar(index_y1, height=y1, width=bar_width, color='#499c9f', label='流失')
plt.bar(index_y2,height=y2, width=bar_width, color='#c76813', label='未流失')
plt.legend(bbox_to_anchor=(0.27, 1)) 
plt.xticks(index_y1 + bar_width/2,x) 
plt.show()

#是否订阅电影频道与客户流失的关系直方图
ax = plt.subplots(figsize=(5, 4))
count1 = len(data[(data["是否订阅电影频道"] == 0 ) & (data["churn"] == 0 )])
count2 = len(data[(data["是否订阅电影频道"] == 0 ) & (data["churn"] == 1 )])
count3 = len(data[(data["是否订阅电影频道"] == 1 ) & (data["churn"] == 0 )])
count4 = len(data[(data["是否订阅电影频道"] == 1 ) & (data["churn"] == 1 )])

x=['订阅电影频道','未订阅电影频道']
y1=[count1,count3]
y2=[count2,count4]

bar_width = 0.3
index_y1 = np.arange(len(x)) # 流失条形图的横坐标
index_y2 = index_y1 + bar_width # 未流失条形图的横坐标
plt.bar(index_y1, height=y1, width=bar_width, color='#499c9f', label='流失')
plt.bar(index_y2,height=y2, width=bar_width, color='#c76813', label='未流失')
plt.legend(bbox_to_anchor=(0.27, 1)) 
plt.xticks(index_y1 + bar_width/2,x) 
plt.show()



#近九个月达到下载限制次数与客户流失的箱线图
filtered_data = data[(data['近九个月达到下载限制次数'] != 0) & (data['近九个月达到下载限制次数'] != 1)& (data['近九个月达到下载限制次数'] != 2)]
df_boxplot = filtered_data[['churn', '近九个月达到下载限制次数']]  
sn.boxplot(x='churn', y='近九个月达到下载限制次数', data=df_boxplot)
plt.gca().get_yaxis().set_major_locator(plt.MaxNLocator(integer=True))#纵坐标为整数
plt.title('近九个月达到下载限制次数与流失情况的关系')
plt.xlabel('流失情况')
plt.ylabel('达到下载限制次数')
plt.show()

#近三个月互联网使用情况与客户流失的箱线图（极值处理
df_boxplot = filtered_data[['churn', '近三个月互联网使用情况']]  
sn.boxplot(x='churn', y='近三个月互联网使用情况', data=df_boxplot)
plt.gca().get_yaxis().set_major_locator(plt.MaxNLocator(integer=True))#纵坐标为整数
plt.title('近三个月互联网使用情况与流失情况的关系')
plt.xlabel('流失情况')
plt.ylabel('互联网使用情况')
plt.show()

#已使用年限与客户流失的箱线图
df_boxplot = filtered_data[['churn', '已使用年限']]  
sn.boxplot(x='churn', y='已使用年限', data=df_boxplot)
plt.gca().get_yaxis().set_major_locator(plt.MaxNLocator(integer=True))#纵坐标为整数
plt.title('已使用年限与流失情况的关系')
plt.xlabel('流失情况')
plt.ylabel('已使用年限')
plt.show()

#相关系数图
data.drop(['id','churn'], axis=1, inplace=True) 
corr = data.corr()
ax = plt.subplots(figsize=(8, 5))
ax = sn.heatmap(corr, vmax=.8, square=True,annot=True,cmap='coolwarm')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.show()

#检测各列空值数占比图
plt.figure(figsize=(8,3))
data.isnull().sum().sort_values(ascending=True).plot(kind='barh')
plt.title("空值情况")
plt.show()

