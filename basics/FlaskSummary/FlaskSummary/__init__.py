from flask import Flask
from .views import account, home


def create_app():

    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')

    # 注册蓝图
    app.register_blueprint(account.account)
    app.register_blueprint(home.home)

    return app
