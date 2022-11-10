# -*- coding = utf-8 -*-
# @Time : 2022/11/10 13:39
# @Author : CZJ
# @File  :   coMap.py
# @software : PyCharm
import plotly.figure_factory as ff
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd



def getColMap():
    # 对每一列的值进行编码
    csv_path = '../ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)

    catcol = ["experience_level", "employment_type", "job_title", "employee_residence", "remote_ratio", "company_location",
              "company_size"]
    encoder = LabelEncoder()
    for col in catcol:
        df[col] = encoder.fit_transform(df[col])

    # 去除无效列
    df.drop(columns='salary_currency', inplace=True)

    # 计算相关系数，转换成矩阵
    df = df.corr()
    dfArr = np.array(df)

    # 设置小数点位数
    dfArr = np.around(dfArr, 3)

    # 两个轴，可以任意指定
    xNames = ["Work Year", "Experience Level", "Employment Type", "Job Title", 'Salary', "Employee Residence",
              "Remote Ratio", "Company Location", "Company Size"]

    # 显示的文本内容
    # z_text = dfArr

    fig = ff.create_annotated_heatmap(
        dfArr,
        x=xNames,
        y=xNames,
        # annotation_text=z_text, # 标注文本内容
        colorscale='Viridis',
        showscale=True
    )
    fig.update_layout(
        title='Employee Correlation Of Features'
    )
    fig.update_xaxes(side="bottom")

    # 字体大小设置
    for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 12
    return fig
