# -*- coding = utf-8 -*-
# @Time : 2022/11/10 16:57
# @Author : CZJ
# @File  :   salaryEploy.py
# @software : PyCharm
# -*- coding = utf-8 -*-
# @Time : 2022/11/10 16:48
# @Author : CZJ
# @File  :   salaryCompany.py
# @software : PyCharm
import pandas as pd
import plotly.express as px

def getSalaryinEmp():
    #数据的处理操作
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)

    # counts = df.groupby(['employee_residence', 'salary_in_usd']).agg(['count'])
    # temp_map = pd.DataFrame(counts)
    # temp_map.reset_index(inplace=True)
    # temp_map = temp_map.loc[temp_map['count']>6]
    # temp_map = pd.DataFrame.sort_values(temp_map, by='mean')
    # fig = px.box(
    #     temp_map,
    #     title='Salary In Different Employee Residences',
    #     x='employee_residence',
    #     y='mean',
    #     template='plotly_dark'
    # )
    # fig.update_layout(
    #     font=dict(size=18, family="Franklin Gothic"),
    #     yaxis_title="Salary(Mean)",
    #     xaxis_title="Employee Residence"
    #     )
    counts = df.groupby('employee_residence')['salary_in_usd'].agg(['count', 'mean'])
    temp_map = pd.DataFrame(counts)
    temp_map.reset_index(inplace=True)
    temp_map = temp_map.loc[temp_map['count'] > 6]
    temp_map = pd.DataFrame.sort_values(temp_map, by='mean')
    areas = temp_map.employee_residence.values.tolist()

    temp = df.loc[df['employee_residence'].isin(areas)]
    fig = px.box(
        temp,
        title='Salary In Different Employee Residences',
        x='employee_residence',
        y='salary_in_usd',
        template='plotly_dark'
    )
    fig.update_layout(
        xaxis_title="Employee Residence",
        yaxis_title="Salary",
        font=dict(size=18, family="Franklin Gothic")
    )
    return fig
