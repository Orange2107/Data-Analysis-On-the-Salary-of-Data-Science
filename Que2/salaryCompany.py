# -*- coding = utf-8 -*-
# @Time : 2022/11/10 16:48
# @Author : CZJ
# @File  :   salaryCompany.py
# @software : PyCharm
import pandas as pd
import plotly.express as px

def getSalaryinDiffCom():
    #数据的处理操作
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)

    counts = df.groupby('company_location')['salary_in_usd'].agg(['count','median'])
    temp_map = pd.DataFrame(counts)
    temp_map.reset_index(inplace=True)

    temp_map = temp_map.loc[temp_map['count']>6]
    temp_map = pd.DataFrame.sort_values(temp_map, by='median')
    fig = px.histogram(
        temp_map,
        title='Salary In Different Company Locations',
        x='company_location',
        y='median',
        template='plotly_dark'
    )
    fig.update_layout(
        font=dict(size=18, family="Franklin Gothic"),
        yaxis_title="Salary(Median)",
        xaxis_title="Company Location"
        )
    return fig
