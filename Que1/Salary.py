# -*- coding = utf-8 -*-
# @Time : 2022/11/8 10:19
# @Author : CZJ
# @File  :   Salary.py
# @software : PyCharm

import pandas as pd
import plotly.express as px
def getSalaryDis():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    fig = px.histogram(df, x='salary_in_usd', template='plotly_dark', title='Distribution of Salary(USD)',nbins=100,text_auto=True,marginal='violin')#nbins 单列的宽度
    #更新布局信息
    fig.update_layout(
        xaxis_title="Salary(USD) ",
        yaxis_title="Count",
        font=dict(size=17,family="Franklin Gothic"),
    )
    return fig