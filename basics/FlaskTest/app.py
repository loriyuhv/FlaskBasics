# 导入Flask，render_template类
from flask import Flask, render_template
import pymysql, numpy as np

# Flask类接收一个参数__name__
app = Flask(__name__)


# 装饰器的作用是将路由映射到视图函数
# 借款金额分布——柱状图
@app.route('/1')
def bar():
    data = GetData()
    # print(data)
    xData = []
    yData = []
    for i in data:
        xData.append(i[0])
        yData.append(i[1])
    return render_template("bar.html", data={"xData": xData, "yData": yData})
    pass


# 借款等级分布图——堆叠条形图
@app.route("/2")
def double_bar():
    data = GetData()
    # print(data)
    fData = []
    vData = []
    grade = [1, 2, 3, 4, 5]
    for j in range(0, 5):
        for i in range(j * 7, j * 7 + 7):
            vData.append(data[i][2])
        # print(fData[j])
        fData.append({"category": grade[j], "value": vData})
        vData = []

    return render_template("double_bar.html", data=fData)
    pass


# 借款等级与借款金额分布图——堆叠条形图
@app.route("/3")
def grade_amount():
    data = GetData()
    fData = []
    vData = []
    grade = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for j in range(0, len(grade)):
        for i in range(j * 5, j * 5 + 5):
            vData.append(data[i][2])
        # print(fData[j])
        fData.append({"category": grade[j], "value": vData})
        vData = []

    return render_template("grade_amount.html", data=fData)
    pass


def GetData():
    # 连接数据库
    connect = pymysql.connect(
        host="localhost",
        user="root",
        password="@wsw0420",
        database="test",
        charset="utf8"
    )
    cursor = connect.cursor()
    # 1借款金额分布
    # cursor.execute("SELECT * FROM loan_amount ORDER BY CAST(SUBSTRING_INDEX(zone,'-',1) AS SIGNED);")
    # 2借款等级分布 需要注释掉上一条命令
    # cursor.execute("SELECT * FROM loan_grade ORDER BY RIGHT(subgrade,1),grade")
    # 3借款等级与借款金额的关系 需要注释掉上一条命令
    cursor.execute("SELECT * FROM grade_amount ORDER BY grade,CAST(SUBSTRING_INDEX(amount,'-',1) AS SIGNED)")
    # 从mysql提取数据到data
    data = cursor.fetchall()
    print(data)
    cursor.close()
    connect.close()
    return [i for i in data]


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(debug=True)
