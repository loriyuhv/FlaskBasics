import pymysql


def GetData():
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

    data = cursor.fetchall()
    print(data)

    cursor.close()
    connect.close()

GetData()