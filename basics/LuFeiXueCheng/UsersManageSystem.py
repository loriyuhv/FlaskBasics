from flask import Flask, render_template, request, redirect

app = Flask(__name__)   # 一个Flask类的对象


@app.route('/login', methods=["GET", "POST"])
def login():
    print("请求来了")
    # 请求方式：如果是GET就进入登录页面，否则就是POST请求
    if request.method == "GET":
        print("GET请求！！！")
        return render_template("login.html")

    # 获取GET穿过来的值
    # url = request.args.get("url")
    print("POST请求！！！")

    # 以下是POST请求
    # 获取POST传过来的值 user, pwd
    user = request.form.get("user")
    pwd = request.form.get("pwd")

    if user == "jerry" and pwd == "12345":
        return redirect("/hello")
    else:
        # return render_template("login.html", **{"msg": "用户名或密码错误！！！"})
        print("用户名或密码错误！！！")
        # return render_template("login.html", msg="用户名或密码错误！！！")
        return render_template("login.html", content="用户名或密码错误")


@app.route("/hello")
def print_hello():
    return "<h3>hello boy!</h3>"


if __name__ == '__main__':
    app.run(debug=True)   # run_simple(host, port, app)
