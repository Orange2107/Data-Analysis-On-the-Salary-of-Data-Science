# -*- coding = utf-8 -*-
# @Time : 2022/11/8 11:18
# @Author : CZJ
# @File  :   salaryDiffCom.py
# @software : PyCharm

import pandas as pd
import plotly.express as px

def getSalaryinDiffCom():
    # 数据的处理操作
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    night_colors = ['rgb(210, 102, 167)', 'rgb(118, 100, 175)', 'rgb(231, 67, 140)', 'rgb(228, 74, 55)']
    fig = px.box(df,
                 x="company_size",
                 y="salary_in_usd",
                 color="experience_level",
                 template='plotly_dark',
                 color_discrete_sequence=night_colors,
                 category_orders={'company_size': ['S', 'M', 'L'], 'experience_level': ['EN', 'MI', 'SE', 'EX']}
                 )
    fig.update_layout(xaxis_title="Company Size",
                      yaxis_title="Salary (USD)",
                      font=dict(size=17, family="Franklin Gothic"),
                      title='Salary Distribution In Different Company Size Based on Experience Level',
                      title_font_family="Franklin Gothic",
                      title_font_size=24,
                      legend_font_size=20,)
    return fig