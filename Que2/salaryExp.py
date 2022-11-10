# -*- coding = utf-8 -*-
# @Time : 2022/11/10 15:22
# @Author : CZJ
# @File  :   salaryExp.py
# @software : PyCharm

import plotly.express as px
import pandas as pd



def getSalryExp():
    # 对每一列的值进行编码
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    fig = px.box(
        df,
        title='Salary In Different Experience Level',
        x='experience_level',
        y='salary_in_usd',
        template='plotly_dark',
        category_orders={'experience_level': ['EN', 'MI', 'SE', 'EX']}

    )
    fig.update_layout(
        xaxis_title="Experience Levels",
        yaxis_title="Salary",
        font=dict(size=18, family="Franklin Gothic")
    )

    return fig

