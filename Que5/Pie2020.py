# -*- coding = utf-8 -*-
# @Time : 2022/11/9 16:27
# @Author : CZJ
# @File  :   Pie2020.py
# @software : PyCharm
import pandas as pd
import plotly.express as px


def addName(x):
    if x == 100:
        return 'Fully remote'
    if x == 50:
        return 'Partially remote'
    if x == 0:
        return 'No remote work'

def get2020Pie():
    #数据的预处理操作
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    df['remote_name'] = df['remote_ratio'].apply(func=addName)

    In2020 = df.loc[df['work_year']==2020]

    #%%
    night_colors = ['rgb(72, 52, 78)', 'rgb(118, 72, 109)', 'rgb(185, 203, 211)'] #指定三个个颜色
    fig = px.pie(
                 In2020,  #指定dataframe
                 names='remote_name',   # 指定列
                 title='Proportion of Remote Ratio In 2020',  # 标题
                 color_discrete_sequence=night_colors,
                 template='plotly_dark',)
    #添加属性
    fig.update_traces(textposition='inside',
                      textinfo='percent+label',
                      )
    fig.update_layout(
        font=dict(size=15, family="Franklin Gothic")
    )
    return fig

