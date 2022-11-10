# -*- coding = utf-8 -*-
# @Time : 2022/11/8 15:19
# @Author : CZJ
# @File  :   jobTitleinEn.py
# @software : PyCharm
import pandas as pd
import plotly.express as px

def getJobTitle():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    df1 = df.loc[df['experience_level'] == 'EN']
    temp = df1
    temp = pd.DataFrame(temp)
    temp.reset_index(inplace=True)
    fig = px.pie(temp,
                names='job_title',
                template='plotly_dark',
                color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_traces(textposition='inside',
                      textinfo='percent+label',
    )
    fig.update_layout(xaxis_title="Experience Level",
                      yaxis_title="Sum of Count",
                      font=dict(size=17, family="Franklin Gothic"),
                      title='Distribution of Job Title Base on Entry Level',
                      title_font_family="Franklin Gothic",
                      title_font_size=24,
                      legend_font_size=20)
    return fig