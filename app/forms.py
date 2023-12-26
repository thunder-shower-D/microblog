#!/user/bin/env python
# -*-coding:utf-8 -*-
"""

@File   : forms.py 
@Desc   :
@Author : WANGCHANGGUAN
@Version: 0.0.1
@Time : 2023/12/25 11:08 
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
