# -*- coding = utf-8 -*-
# @Time : 2022/11/11 23:40
# @Author : CZJ
# @File  :   topFiveJob.py
# @software : PyCharm
import plotly.express as px
import pandas as pd



def getTopFive():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    top_job = df.groupby('job_title').size()
    top_job = top_job.sort_values(ascending=False)[:5].index.to_list()  # 转换成list类型 使用isin
    top_job_df = df[df['job_title'].isin(top_job)]
    fig = px.box(top_job_df,
                 x="job_title",
                 y="salary_in_usd",
                 title='Salary Distribution of Top 5 Popular Job Titles',
                 template='plotly_dark')
    fig.update_layout(xaxis_title="Title",
                      yaxis_title="Salary (in USD)",
                      font=dict(size=15, family="Franklin Gothic"),
                      title_font_family="Franklin Gothic",
                     )
    return fig