from flask import Blueprint, render_template
from ..models import Question
from exts import db
from .forms import Question as q

bp = Blueprint('cms', __name__)


@bp.route('/add_questions/', methods=['GET', 'POST'])
def add_questions():
    form = q()
    if form.validate_on_submit():
        subject = form.subject.data
        answer_1 = form.answer_1.data
        answer_2 = form.answer_2.data
        answer_3 = form.answer_3.data
        answer_4 = form.answer_4.data
        right_answer = form.right_answer.data
        print(subject)
        question = Question(subject=subject, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4,
                            right_answer=right_answer)
        db.session.add(question)
        db.session.commit()
    return render_template('cms/add_questions.html', form=form)
