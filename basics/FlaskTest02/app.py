from flask import Flask, render_template, redirect

# 基础
'''
import json

from flask import Flask

# app = Flask(__name__)   # __name__是变量，字符串类型 Flask(模块名字符串)
# app = Flask(__name__, static_url_path='/s', static_folder="static")
app = Flask(__name__)

# 从配置对象中加载
"""
class DefaultConfig(object):
    # 默认配置
    SECRET_KEY = "@haha0420"

app.config.from_object(DefaultConfig)
"""

# 从配置文件中加载
# app.config.from_pyfile('setting.py')


app.config.from_envvar('PROJECT_SETTING', silent=True)

# 打印视图
@app.route('/')
def hello_world():
    print(app.config["SECRET_KEY"])
    return 'Hello World!'

# 打印路由
"""
print(app.url_map)

# 需要遍历url_map 取出特定信息 在一个特定接口返回
for rule in app.url_map.iter_rules():
    print("name={} path={}".format(rule.endpoint, rule.rule))


@app.route('/')
def route_map():
    # 主视图 返回所有视图网址
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})
"""

# if __name__ == '__main__':
#     app.run()
'''

# 处理请求

# url路径参数
# 转换器
"""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# /users/123
@app.route('/users/<int:user_id>')  # 等价于：@app.route('/users/<string:user_id>')
def get_users_data(user_id):
    print(type(user_id))    # <class 'str'>
    return 'get users {}'. format(user_id)


# 创建转换器类，保存匹配的是正则表达式
class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


# 将自定义转换器添加到转换器字典中，并指定转换器使用时的名字为：mobile
app.url_map.converters['mobile'] = MobileConverter


@app.route('/sms_codes/<mobile:mob_num>')
def send_sms_code(mob_num):
    print(type(mob_num))    # <class 'str'>
    return 'send sms code to {}'. format(mob_num)
"""

# 其他参数
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/articles')
def get_articles():
    # 获取请求头中的查询参数
    channel_id = request.args.get("channel_id")
    # 获取请求头中的headers信息
    headers = request.headers.get('Accept-Language')

    return 'you wanna get articles of' \
           ' channel {}, headers: {}'.format(channel_id, headers)
"""

# 处理响应

app = Flask(__name__)


@app.route('/')
def index():
    # 普通传参
    # mstr = "Hello world"
    # mint = 10
    # return render_template('index.html', my_str=mstr, my_int=mint)
    # 传字典
    data = dict(
        my_int=123,
        my_str="hello world"
    )
    print(data)
    print("*"*10)
    # 当函数中以列表或者元组的形式传参时，就要使用 * args；
    # 当传入字典形式的参数时，就要使用 ** kwargs。
    return render_template('index.html', **data)

# 重定向
# from flask import redirect


@app.route('/demo2')
def demo2():
    return redirect('http://www.baidu.com')

# 返回jsonity
from flask import jsonify


@app.route('/demo3')
def demo3():
    json_dict = {
        'user_id': 10,
        'user_name': 'loriyuhv'
    }
    return jsonify(json_dict)

import json


@app.route('/demo4')
def demo4():
    json_dict = {
        'user_id': 10,
        'user_name': 'loriyuhv'
    }
    return json.dumps(json_dict)
