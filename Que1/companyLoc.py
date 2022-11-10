# -*- coding = utf-8 -*-
# @Time : 2022/11/8 10:24
# @Author : CZJ
# @File  :   companyLoc.py
# @software : PyCharm
import pandas as pd
import plotly.express as px
import country_converter as co
def getCompanyLoc():
    csv_path = 'ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)
    df.employee_residence = co.convert(names=df.employee_residence, to='ISO3')
    df.loc[:, 'company_location'] = co.convert(names=df.company_location, to='ISO3')
    temp_se = df.groupby('company_location')['job_title'].count()
    temp_se = pd.DataFrame(temp_se)
    temp_se.columns = ['Count']
    temp_se.reset_index(inplace=True)  # 将地址转换到列
    fig = px.choropleth(
        title="The World Map of Companies Location",
        data_frame=temp_se,  # 需要为DataFrame类型
        locations="company_location",  # 传入ISO3参数确定经纬度
        color='Count',
        color_continuous_scale=px.colors.sequential.Plasma
    )
    fig.update_layout(
        font=dict(size=15, family="Franklin Gothic")
    )
    return fig