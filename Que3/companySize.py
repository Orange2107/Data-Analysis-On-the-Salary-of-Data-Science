# -*- coding = utf-8 -*-
# @Time : 2022/11/8 11:11
# @Author : CZJ
# @File  :   companySize.py
# @software : PyCharm
import pandas as pd
import plotly.express as px

def getCompanySize():
    # 数据的处理操作
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)

    # 进行分组，生成三列
    sizeAndExp = df.groupby(['company_size', 'experience_level'])['work_year'].count()
    sizeAndExp = pd.DataFrame(sizeAndExp)
    sizeAndExp.columns = ['count']
    sizeAndExp.reset_index(inplace=True)

    # 按照经验水平进行颜色区分
    night_colors = ['rgb(210, 102, 167)', 'rgb(118, 100, 175)', 'rgb(231, 67, 140)', 'rgb(228, 74, 55)']
    fig = px.histogram(sizeAndExp,
                       x="company_size",
                       y="count",
                       color="experience_level",  # 对count里的值进行分类
                       color_discrete_sequence=night_colors,
                       barmode='group',
                       template='plotly_dark',
                       category_orders={'company_size': ['S', 'M', 'L'], 'experience_level': ['EN', 'MI', 'SE', 'EX']},
                       text_auto='True')
    fig.update_layout(
        font=dict(size=18, family="Franklin Gothic"),
        title='Counts in Different Company Size Base On Experience Level',
        xaxis_title="Company Size",
        yaxis_title="Experience Level Count",
    )
    return fig
