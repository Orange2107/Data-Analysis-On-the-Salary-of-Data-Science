# -*- coding = utf-8 -*-
# @Time : 2022/11/13 20:45
# @Author : CZJ
# @File  :   hhh.py
# @software : PyCharm
# -*- coding = utf-8 -*-
# @Time : 2022/11/12 23:26
# @Author : CZJ
# @File  :   test.py
# @software : PyCharm
import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score, mean_squared_error, mean_absolute_error, median_absolute_error, r2_score
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def getPre(x_train, x_test, y_train, y_test):

    #model = ensemble.GradientBoostingRegressor()
    model = LR()
    model.fit(x_train, y_train)
    #保存模型
    joblib.dump(model, '../model_LR_test.pkl')

def getUpdatePre():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop_duplicates(inplace=True)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    #df = df.loc[df['salary_in_usd'] <= 276000]
    cat_cols = df.columns.difference(['remote_ratio', 'salary_in_usd', 'work_year'])
    # cat_cols #都是离散型变量

    # 对部分噪声点进行去除
    # 对job title较少的进行去除
    job_title_cat = df.groupby('job_title')['job_title'].agg('count').sort_values(ascending=False)
    job_title_cat_other = job_title_cat[job_title_cat <= 3]
    df.job_title = df.job_title.apply(lambda x: 'other' if x in job_title_cat_other else x)
    # 对较少的employee residence进行去除
    emp_res_cat = df.groupby('employee_residence')['employee_residence'].agg('count').sort_values(ascending=False)
    emp_res_cat_other = emp_res_cat[emp_res_cat <= 2]
    df.employee_residence = df.employee_residence.apply(lambda x: 'other' if x in emp_res_cat_other else x)
    # 对较少的conpany location进行去除
    com_loc_cat = df.groupby('company_location')['company_location'].agg('count').sort_values(ascending=False)
    com_loc_cat_other = com_loc_cat[com_loc_cat <= 2]
    df.company_location = df.company_location.apply(lambda x: 'other' if x in com_loc_cat_other else x)



    for i in cat_cols:
        df[i] = df[i].astype('category')  #离散型 --> 顺序编号
        df[i] = df[i].cat.codes

    # onehot编码后的维度
    for i in cat_cols:
        print(i, df[i].nunique())

    #df = pd.get_dummies(df, columns=['company_size', 'employment_type', 'experience_level',
                                     # 'work_year', 'salary_currency', 'company_location',
                                     # 'job_title', 'employee_residence'])
    df = pd.get_dummies(df, columns=['company_location', 'employee_residence', 'experience_level', 'job_title'])

    x = df.drop('salary_in_usd', axis=1)

    # salary归一化
    temp = df['salary_in_usd']
    temp = (temp - np.min(temp)) / (np.max(temp) - np.min(temp))
    y = temp

    #pca = PCA(n_components=50)
    pca = PCA(n_components=38)
    x = pca.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.25)
    model = LR()
    model.fit(x_train, y_train)
    preds = model.predict(x_test)
    print("R2", model.score(x_test, y_test))
    return preds, y_test

def getJudge(preds, y_test):
    # 评判预测结果
    # 平均绝对误差
    mean_absolute_score = mean_absolute_error(y_pred=preds, y_true=y_test)  # 3.3775517360082032
    # 均方误差
    mean_squared_score = mean_squared_error(y_pred=preds, y_true=y_test)  # 31.15051739031563
    # 中值绝对误差
    median_absolute_score = median_absolute_error(y_pred=preds, y_true=y_test)  # 1.7788996425420773
    # 可解释方差
    explained = explained_variance_score(y_pred=preds, y_true=y_test) # 0.710547565009666
    # R2
    #r2 = r2_score(y_pred=preds, y_true=y_test)  # 0.7068961686076838

    print("平均绝对误差", mean_absolute_score)
    print("均方误差", mean_squared_score)
    print("中值绝对误差", median_absolute_score)
    print("可解释方差", explained)
    #print("R2", r2)

def getImages(preds, y_test):

    predss = preds.tolist()
    y_testt = y_test.tolist()
    p1 = pd.DataFrame(predss)
    p2 = pd.DataFrame(y_testt)
    p1.columns = ['preds']
    p2.columns = ['y_test']
    new = pd.concat([p1, p2], axis=1)
    new.insert(0, 'index', range(len(new)), allow_duplicates=False)

    # 可视化
    fig1 = px.scatter(
        x=y_test,
        y=preds,
        template='plotly_dark'
    )
    fig1.update_layout(title='Scatterplot of true and predicted values',
                      xaxis_title='True Values',
                      yaxis_title='Predicted Values',
                       font=dict(size=17, family="Franklin Gothic"),
                       title_font_size=24,
    )

    fig1.add_shape(
        type="line", line=dict(dash='dash'),
        x0=y_test.min(), y0=y_test.min(),
        x1=y_test.max(), y1=y_test.max()
    )


   #双图层坐标
    trace0 = go.Scatter(
        x=new['index'].values,
        y=new['preds'].values,
        mode='lines',
        name='Predicted')
    trace1 = go.Scatter(
        x=new['index'].values,
        y=new['y_test'].values,
        mode='lines+markers',
        name='True',
        yaxis="y2")

    data1 = [trace0, trace1]

    # go.Layout可以创建图层对象，实现双坐标
    layout = go.Layout(title="双坐标示例图",
                       yaxis=dict(title="Predicted"),
                       template='plotly_dark',
                       yaxis2=dict(title="True", overlaying='y', side="right"),
                       legend=dict(x=0, y=1, font=dict(size=12, color="black")))
    fig2 = go.Figure(data=data1, layout=layout)
    fig2.update_layout(title='Line of true and predicted values',
                      xaxis_title='Counts',
                      font=dict(size=17, family="Franklin Gothic"),
                      title_font_size=24,

    )
    return fig1, fig2


def getData():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop_duplicates(inplace=True)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    df = df.loc[df['salary_in_usd'] < 276000]
    cat_cols = df.columns.difference(['remote_ratio', 'salary_in_usd'])

    # cat_cols #都是离散型变量

    for i in cat_cols:
        df[i] = df[i].astype('category')  # 离散型 --> 顺序编号
        df[i] = df[i].cat.codes

    # onehot编码后的维度
    for i in cat_cols:
        print(i, df[i].nunique())

    # df = pd.get_dummies(df, columns=['company_size', 'employment_type', 'experience_level', 'work_year', 'salary_currency','company_location', 'company_size'])
    df = pd.get_dummies(df, columns=['company_location', 'employee_residence', 'experience_level'])
    # 111维度
    x = df.drop('salary_in_usd', axis=1)

    # salary归一化
    temp = df['salary_in_usd']
    temp = (temp - np.min(temp)) / (np.max(temp) - np.min(temp))
    y = temp

    # pca = PCA(n_components=50)
    pca = PCA(n_components=18)
    x = pca.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.25)
    return x_train, x_test, y_train, y_test


def main():
    x_train, x_test, y_train, y_test = getData()
    # 训练模型
    # getPre(x_train, x_test, y_train, y_test)
    model = joblib.load('model_LR_test.pkl')
    preds = model.predict(x_test)
    getJudge(preds, y_test)
    fig1, fig2 = getImages(preds, y_test)
    return fig1, fig2


