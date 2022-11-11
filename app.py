from flask import Flask, render_template
import json
import plotly as py
from Que1 import expDis, workType, expPie, Salary, companyLoc, employLoc, remotePie, overseaDis
from Que3 import companySize, salaryDiffCom, diffExpinCom, jobTitleinEn, topFiveJob
from Que5 import countsMeanSalary, Pie2020, Pie2021, Pie2022
from Que2 import coMap, salaryExp, salaryCompany, salaryEploy

app = Flask(__name__)  # 初始化网页对象


# 返回给用户渲染后的网页
@app.route('/')
def index():
    return render_template("index.html")  # 写入var中传入前端页面，render进行符号解析，把var进行替换

@app.route('/que1')
def Que1():
    fig1 = expDis.getExpLevel()
    fig2 = workType.getWorkType()
    fig3 = expPie.getExpPie()
    fig4 = Salary.getSalaryDis()
    fig5 = companyLoc.getCompanyLoc()
    fig6 = employLoc.getEmployLoc()
    fig7 = remotePie.getRemotePie()
    fig8 = overseaDis.getOverseasDis()
    graphJSON = json.dumps(fig1, cls=py.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=py.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=py.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=py.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(fig5, cls=py.utils.PlotlyJSONEncoder)
    graphJSON6 = json.dumps(fig6, cls=py.utils.PlotlyJSONEncoder)
    graphJSON7 = json.dumps(fig7, cls=py.utils.PlotlyJSONEncoder)
    graphJSON8 = json.dumps(fig8, cls=py.utils.PlotlyJSONEncoder)
    return render_template("que1.html", graphJSON=graphJSON,  # 写入var中传入前端页面，render进行符号解析，把var进行替换
                           graphJSON2=graphJSON2,
                           graphJSON3=graphJSON3,
                           graphJSON4=graphJSON4,
                           graphJSON5=graphJSON5,
                           graphJSON6=graphJSON6,
                           graphJSON7=graphJSON7,
                           graphJSON8=graphJSON8)

@app.route('/que2')
def Que2():
    fig = coMap.getColMap()
    fig2 = salaryExp.getSalryExp()
    fig3 = salaryCompany.getSalaryinDiffCom()
    fig4 = salaryEploy.getSalaryinEmp()
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=py.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=py.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=py.utils.PlotlyJSONEncoder)
    return render_template("que2.html", graphJSON=graphJSON,
                           graphJSON2=graphJSON2,
                           graphJSON3=graphJSON3,
                           graphJSON4=graphJSON4,
                           )  # 写入var中传入前端页面，render进行符号解析，把var进行替换

@app.route('/que3')
def Que3():
    fig1 = companySize.getCompanySize()
    fig2 = salaryDiffCom.getSalaryinDiffCom()
    fig3 = diffExpinCom.getDiffExp()
    fig4 = jobTitleinEn.getJobTitle()
    fig5 = topFiveJob.getTopFive()
    graphJSON = json.dumps(fig1, cls=py.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=py.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=py.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=py.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(fig5, cls=py.utils.PlotlyJSONEncoder)

    return render_template("que3.html",
                           graphJSON=graphJSON,
                           graphJSON2=graphJSON2,
                           graphJSON3=graphJSON3,
                           graphJSON4=graphJSON4,
                           graphJSON5=graphJSON5
                           )  # 写入var中传入前端页面，render进行符号解析，把var进行替换

@app.route('/que4')
def Que4():
    return render_template('que5.html')

@app.route('/que5')
def Que5():
    fig1 = countsMeanSalary.getCountsSalary()
    fig2 = Pie2020.get2020Pie()
    fig3 = Pie2021.get2021Pie()
    fig4 = Pie2022.get2022Pie()
    graphJSON = json.dumps(fig1, cls=py.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=py.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=py.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=py.utils.PlotlyJSONEncoder)
    return render_template("que5.html",
                           graphJSON=graphJSON,
                           graphJSON2=graphJSON2,
                           graphJSON3=graphJSON3,
                           graphJSON4=graphJSON4
                           )  # 写入var中传入前端页面，render进行符号解析，把var进行替换


if __name__ == '__main__':
    app.run()
