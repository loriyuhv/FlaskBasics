from flask import Blueprint, render_template, request, session, redirect
from uuid import uuid4

home = Blueprint("home", __name__)


@home.route('/index')
def index():
    user_info = session.get('user_info')
    print(user_info)

    return "index"


@home.route('/test')
def test():
    user_info = session.get('user_info')
    print(user_info)
    return "test"
