"""
该程序主要用于学习蓝图对象的基本知识
"""
from flask import Flask, Blueprint

app = Flask(__name__)

# 创建蓝图对象
user_bp = Blueprint('user', __name__)


@user_bp.route('/profile')
def get_profile():
    return "User profile"


# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/user')

from goods import goods_bp
app.register_blueprint(goods_bp)


if __name__ == "__main__":
    app.run(Debug=True)
