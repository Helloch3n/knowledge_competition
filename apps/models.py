from exts import db
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dl_id = db.Column(db.String(6), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    # num_of_answers = db.Column(db.Integer, default=1)


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    subject = db.Column(db.Text, nullable=False)
    answer_1 = db.Column(db.Text, nullable=False)
    answer_2 = db.Column(db.Text, nullable=False)
    answer_3 = db.Column(db.Text, nullable=False)
    answer_4 = db.Column(db.Text, nullable=False)
    right_answer = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'answer_1': self.answer_1,
            'answer_2': self.answer_2,
            'answer_3': self.answer_3,
            'answer_4': self.answer_4,
            'right_answer': self.right_answer,
        }


class Answer_record(db.Model):
    __tablename__ = 'answer_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    score = db.Column(db.Integer)
    start_time = db.Column(db.DateTime)
    submit_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    integral = db.Column(db.DECIMAL(2, 1))

    user = relationship('User', backref='answer_record')
