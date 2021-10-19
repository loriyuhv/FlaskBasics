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
    xData = []
    yData = []
    for i in data:
        xData.append(i[1])
        yData.append(i[0])
    return render_template("bar.html", data={"xData": xData, "yData": yData})
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
    cursor.execute("SELECT * FROM loan_amount;")
    # 从mysql提取数据到data
    data = cursor.fetchall()

    cursor.close()
    connect.close()
    return [i for i in data]


# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run(debug=True)
