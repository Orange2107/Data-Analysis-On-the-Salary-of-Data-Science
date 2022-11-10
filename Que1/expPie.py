# -*- coding = utf-8 -*-
# @Time : 2022/11/8 10:00
# @Author : CZJ
# @File  :   exp_pie.py
# @software : PyCharm
import pandas as pd
import plotly.express as px
def getExpPie():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    night_colors = ['rgb(72, 52, 78)', 'rgb(118, 72, 109)', 'rgb(185, 203, 211)', 'rgb(98, 142, 143)'] #指定四个板块的颜色
    fig = px.pie(df,
             names='experience_level',
             title='Proportion of Experience Level',
             color_discrete_sequence=night_colors,
             template = 'plotly_dark',
             )
    #添加属性
    fig.update_traces(textposition='inside',
                  textinfo='percent+label',
                  textfont_size=20,
                  )
    return fig