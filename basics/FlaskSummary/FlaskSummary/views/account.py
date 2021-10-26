from flask import Blueprint, render_template, request, session, redirect
from uuid import uuid4

account = Blueprint("account", __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'alex' and pwd == '123':
        uid = str(uuid4())
        session["user_info"] = {"id": uid, 'name': user}
        return redirect('/index')
    else:
        return render_template('login.html', msg='用户名或密码错误')
