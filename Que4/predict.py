# -*- coding = utf-8 -*-
# @Time : 2022/11/10 18:18
# @Author : CZJ
# @File  :   predict.py
# @software : PyCharm
import pickle

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.linear_model import LinearRegression as LR
from sklearn import tree
import pandas as pd
from sklearn.model_selection import cross_val_predict, train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
from sklearn.svm import SVC


def dataSet():
    def getClass(x):
        if x <= 62726:
            return 0
        if x <101570 and x > 62726:
            return 1
        else:
            return 2



    # 数据的处理操作
    csv_path = '../ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    df.drop(columns='salary_currency', inplace=True)
    df['tabel'] = df['salary_in_usd'].apply(func=getClass)

    #对salary进行划分标签
    #进行编码
    catcol = ["experience_level", "employment_type", "job_title", "employee_residence",
              "remote_ratio", "company_location", "company_size", 'work_year']
    encode = LE()
    for col in catcol:
        df[col] = encode.fit_transform(df[col])  #归一化
        str = col+'.pickle'
        doc = open(str, "wb")
        pickle.dump(encode, doc)  # 保存机型编码模型
        doc.close()

    #对离散数据进行one hot编码

    pca = PCA(n_components=3)

    x = df[["experience_level", "employment_type", "job_title", "employee_residence",
              "remote_ratio", "company_location", "company_size", 'work_year']]

    x = pca.fit_transform(x)
    y = df['tabel']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    return  x_train, x_test, y_train, y_test

def train(x, y):
    #Linear Regression
    # model = LR()
    # model.fit(x, y)

    # model = LR()
    # model.fit(x, y)

    #SVM

    #model = SVC(random_state=3)
    #model = SVC(random_state=4, kernel="linear")
    #model = SVC(random_state = 2, kernel="sigmoid")
    #model = SVC(random_state = 4, kernel="poly", degree=4)
    #classifier.fit(x, y)

    #Tree
    #model = tree.DecisionTreeClassifier(splitter='random')

    model.fit(x_train, y_train)
    return model

def test(model,x,y):

    y_predictt = model.predict(x)
    accuracy = metrics.accuracy_score(y_true=y, y_pred=y_predictt)
    print(accuracy)
    matrix = metrics.confusion_matrix(y, y_predictt, labels=[0, 1, 2])

    disp = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=[0,1,2])
    disp.plot(
        include_values=True,  # 混淆矩阵每个单元格上显示具体数值
        cmap="viridis",  # 不清楚啥意思，没研究，使用的sklearn中的默认值
        ax=None,  # 同上
        xticks_rotation="horizontal",  # 同上
        values_format="d"  # 显示的数值格式
    )
    plt.show()


# def predict(model,exp,com,emp):
#     exp_pkl = open('experience_level.pickle', 'rb')
#     exp_encoder = pickle.load(exp_pkl)
#     exp_pkl.close()
#     x1 = exp_encoder.transform([exp])[0]
#
#     com_pkl = open('company_location.pickle', 'rb')
#     com_encoder = pickle.load(com_pkl)
#     com_pkl.close()
#     x2 = com_encoder.transform([com])[0]
#
#     emp_pkl = open('employee_residence.pickle', 'rb')
#     emp_encoder = pickle.load(emp_pkl)
#     emp_pkl.close()
#     x3 = emp_encoder.transform([emp])[0]
#     salary = model.predict([[x1, x2, x3]])
#     return salary



## 测试代码
if __name__ == '__main__':
    x_train, x_test, y_train, y_test = dataSet()
    model = train(x_train, y_train)
    test(model, x_test, y_test)
