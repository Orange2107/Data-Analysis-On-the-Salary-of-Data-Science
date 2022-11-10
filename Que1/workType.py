# -*- coding = utf-8 -*-
# @Time : 2022/11/7 18:27
# @Author : CZJ
# @File  :   workType.py
# @software : PyCharm
import pandas as pd
import plotly.express as px
def getWorkType():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    fig = px.histogram(df, x='employment_type', template='plotly_dark', title='Distribution of Employment Type',
                       text_auto=True)
    fig.update_layout(
        xaxis_title="Employment Type",
        yaxis_title="Count",
        font=dict(size=17, family="Franklin Gothic"),
    )
    return fig
