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
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)

    catcol = ["experience_level", "employment_type", "job_title", "remote_ratio", "company_location",
              "company_size"]
    encoder = LabelEncoder()
    for col in catcol:
        if col == 'experience_level' and 'company_size':
            continue
        df[col] = encoder.fit_transform(df[col])
    df['experience_level'] = df['experience_level'].replace('EN', 0)
    df['experience_level'] = df['experience_level'].replace('MI', 1)
    df['experience_level'] = df['experience_level'].replace('SE', 2)
    df['experience_level'] = df['experience_level'].replace('EX', 3)

    df['company_size'] = df['company_size'].replace('S', 0)
    df['company_size'] = df['company_size'].replace('M', 1)
    df['company_size'] = df['company_size'].replace('L', 2)



    # 去除无效列
    df.drop(columns='salary_currency', inplace=True)

    # 计算相关系数，转换成矩阵
    df = df.corr()
    dfArr = np.array(df)

    # 设置小数点位数
    dfArr = np.around(dfArr, 3)

    # 两个轴，可以任意指定
    xNames = ["Work Year", "Experience Level", "Employment Type", "Job Title", 'Salary',
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
    fig.update_xaxes(side="bottom")
    fig.update_layout(
            font=dict(size=15, family="Franklin Gothic"),
            title='Employee Correlation Of Features',
            title_font_family="Franklin Gothic",
            title_font_size=24
    )
    return fig
