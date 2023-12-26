#!/user/bin/env python
# -*-coding:utf-8 -*-
"""

@File   : __init__.py 
@Desc   :
@Author : WANGCHANGGUAN
@Version: 0.0.1
@Time : 2023/12/21 17:13 
"""
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__, template_folder=r'E:\pythonProject\microblog\app\templates')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models