# -*- coding = utf-8 -*-
# @Time : 2022/11/8 15:14
# @Author : CZJ
# @File  :   diffExpinCom.py
# @software : PyCharm
import pandas as pd
import plotly.express as px

def getDiffExp():
    # 数据的处理操作
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    temp = df.groupby(['experience_level','job_title'])['work_year'].count()
    temp = pd.DataFrame(temp)
    temp.columns = ['count']
    temp.reset_index(inplace=True)
    fig = px.histogram(temp,
                       x="experience_level",
                       y="count",
                       color="job_title",
                       template='plotly_dark',
                       color_discrete_sequence=px.colors.sequential.RdBu,
                       category_orders={'experience_level':['EN','MI','SE','EX']})
    fig.update_layout(xaxis_title="Experience Level",
                      yaxis_title="Sum of Count",
                      font=dict(size=17,family="Franklin Gothic"),
                      title='Sum of Count In Different Experience Level Based on Job Title',
                      title_font_family="Franklin Gothic",
                      title_font_size=24,
                      legend_font_size=20, )
    return fig

