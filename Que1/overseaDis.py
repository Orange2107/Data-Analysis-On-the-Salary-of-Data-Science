# -*- coding = utf-8 -*-
# @Time : 2022/11/8 10:55
# @Author : CZJ
# @File  :   overseaDis.py
# @software : PyCharm
import pandas as pd
import plotly.express as px
# 增加overseas列，定义company location != employee residence 为 True
def defineOverseas(x):
    if x.employee_residence == x.company_location:
        return "False"
    else:
        return "True"

def getOverseasDis():
    #数据的处理操作
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    #新增一列
    df['Overseas'] = df.apply(lambda x: defineOverseas(x), axis=1)
    fig = px.histogram(
        data_frame=df,
        title='Distribution of Overseas Employees',
        x='Overseas',
        text_auto=True,
        template='plotly_dark',
    )
    fig.update_layout(
        font=dict(size=18, family="Franklin Gothic"),
        yaxis_title="Count",
    )
    return fig

