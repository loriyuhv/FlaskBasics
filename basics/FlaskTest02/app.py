import json

from flask import Flask

# app = Flask(__name__)   # __name__是变量，字符串类型 Flask(模块名字符串)
# app = Flask(__name__, static_url_path='/s', static_folder="static")
app = Flask(__name__)

# 从配置对象中加载
'''
class DefaultConfig(object):
    """默认配置"""
    SECRET_KEY = "@haha0420"

app.config.from_object(DefaultConfig)
'''

# 从配置文件中加载
'''
# app.config.from_pyfile('setting.py')
'''

app.config.from_envvar('PROJECT_SETTING', silent=True)

# 打印视图
@app.route('/')
def hello_world():
    print(app.config["SECRET_KEY"])
    return 'Hello World!'

# 打印路由
'''
print(app.url_map)

# 需要遍历url_map 取出特定信息 在一个特定接口返回
for rule in app.url_map.iter_rules():
    print("name={} path={}".format(rule.endpoint, rule.rule))


@app.route('/')
def route_map():
    """
    主视图 返回所有视图网址
    :return:
    """
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})
'''

# if __name__ == '__main__':
#     app.run()
