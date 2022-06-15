from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import InputRequired


class Question(FlaskForm):
    subject = StringField(validators=[InputRequired(message='请输入题目')])
    answer_1 = StringField(validators=[InputRequired(message='请输入题目')])
    answer_2 = StringField(validators=[InputRequired(message='请输入题目')])
    answer_3 = StringField(validators=[InputRequired(message='请输入题目')])
    answer_4 = StringField(validators=[InputRequired(message='请输入题目')])
    right_answer = IntegerField(validators=[InputRequired(message='请输入正确答案序号')])
