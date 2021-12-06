from flask import Flask, render_template

app = Flask(__name__)   # 一个Flask类的对象


@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)   # run_simple(host, port, app)


