# -*- coding = utf-8 -*-
# @Time : 2022/11/8 10:37
# @Author : CZJ
# @File  :   remotePie.py
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

def getRemotePie():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    df['remote_name'] = df['remote_ratio'].apply(func=addName)
    night_colors = ['rgb(72, 52, 78)', 'rgb(118, 72, 109)', 'rgb(185, 203, 211)']  # 指定三个个颜色
    fig = px.pie(df,  # 指定dataframe
                 names='remote_name',  # 指定列
                 title='Proportion of Remote Ratio',  # 标题
                 color_discrete_sequence=night_colors,
                 template='plotly_dark',
                 )
    # 添加属性
    fig.update_traces(textposition='inside',
                      textinfo='percent+label',
                      )
    fig.update_layout(
        font=dict(size=18, family="Franklin Gothic")
    )
    return fig
