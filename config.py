#!/user/bin/env python
# -*-coding:utf-8 -*-
"""

@File   : config.py 
@Desc   :
@Author : WANGCHANGGUAN
@Version: 0.0.1
@Time : 2023/12/25 10:35 
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')