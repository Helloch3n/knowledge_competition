from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class User(FlaskForm):
    dl_id = StringField(validators=[InputRequired(message='请输入工号')])
    username = StringField(validators=[InputRequired(message='请输入姓名')])
