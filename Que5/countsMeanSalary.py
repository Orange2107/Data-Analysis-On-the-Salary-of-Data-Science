# -*- coding = utf-8 -*-
# @Time : 2022/11/9 16:08
# @Author : CZJ
# @File  :   countsMeanSalary.py
# @software : PyCharm
import pandas as pd
import plotly.graph_objs as go
import numpy as np

def getCountsSalary():
    #数据的预处理操作
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)

    #进行分类
    temp = df.groupby(['work_year'])['salary_in_usd'].agg(['count', 'mean'])
    # %%
    temp = pd.DataFrame(temp)
    temp.reset_index(inplace=True)
    col = np.array(temp['mean'])
    col2 = np.array(temp['count'])
    trace1 = go.Bar(
        x=['2020', '2021', '2022'],
        y=col,
        name='Salary'
    )
    trace2 = go.Scatter(
        x=['2020', '2021', '2022'],
        y=col2,
        name='Count',
        xaxis='x',
        yaxis='y2'#标明设置一个不同于trace1的一个坐标轴
    )

    data = [trace1, trace2]
    layout = go.Layout(
        yaxis2=dict(anchor='x', overlaying='y', side='right')#设置坐标轴的格式，一般次坐标轴在右侧
    )

    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(
                      template = 'plotly_dark',
                      font = dict(size=13,family="Franklin Gothic"),
                      title = 'Employee Counts and Mean Salary During the Epidemic',
                      title_font_family = "Franklin Gothic",
                    )
    return fig