# -*- coding = utf-8 -*-
# @Time : 2022/11/7 17:03
# @Author : CZJ
# @File  :   exp_level.py
# @software : PyCharm
import pandas as pd
import plotly.express as px
def getExpLevel():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    fig = px.histogram(df, x='experience_level', template='plotly_dark', title='Distribution of Experience Level',category_orders={'experience_level' : ['EN', 'MI', 'SE', 'EX']}, text_auto=True)
    fig.update_layout(
        xaxis_title="Experience Level",
        yaxis_title="Count",
        font=dict(size=17, family="Franklin Gothic")
    )
    return fig
