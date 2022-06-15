from flask import Blueprint, render_template, jsonify, views, redirect, url_for, session, g, request
from exts import db
from ..models import Question, User, Answer_record
import random
from .forms import User as u
from config import FRONT_USER_ID, SELECTED, TRUTH, TIME_LIMIT, START_TIME, END_TIME, SUBMIT_LIMIT
from .decorators import login_required
import traceback
from flask_cors import CORS
from exts import csrf
import datetime

bp = Blueprint("front", __name__)
CORS(bp)


# 填写答题者信息
class Respondent(views.MethodView):
    def post(self):
        form = u()
        dl_id = form.dl_id.data
        username = form.username.data
        # 如果不是第一次答题，判断今日答题次数是否超过三次
        if User.query.filter_by(dl_id=dl_id).first():
            user = User.query.filter_by(dl_id=dl_id).first()
            session[FRONT_USER_ID] = user.dl_id
            records = Answer_record.query.filter(Answer_record.user_id == user.id).all()
            nums = []
            # 超过三次则不允许再答题
            for record in records:
                # print(datetime.datetime.date(record.start_time))
                if datetime.datetime.date(record.start_time) == datetime.date.today():
                    nums.append(record)
                # print(nums)
            if len(nums) >= SUBMIT_LIMIT:
                return redirect(url_for('front.notice'))
            # 未超过三次记录本次答题记录
            else:
                answer_record = Answer_record(start_time=datetime.datetime.now())
                user.answer_record.append(answer_record)
                db.session.commit()
                return redirect(url_for('front.index'))
        # 如果是第一次答题，则保存答题者信息
        else:
            user = User(dl_id=dl_id, username=username)
            answer_record = Answer_record(start_time=datetime.datetime.now())
            user.answer_record.append(answer_record)
            db.session.add(user)
            db.session.commit()
            session[FRONT_USER_ID] = user.dl_id
            return redirect(url_for('front.index'))

    def get(self):
        form = u()
        return render_template('front/respondent.html', form=form)


bp.add_url_rule('/respondent/', view_func=Respondent.as_view('respondent'))


# 超过三次提示
@bp.route('/notice/')
@login_required
def notice():
    return render_template('front/notice.html')


# 题目界面
@bp.route('/')
@login_required
def index():
    return render_template('front/index.html')


# 题目界面_ajax_get,计算正确答案
@bp.route('/question/')
def question():
    questions = db.session.query(Question).all()
    results = random.sample(range(0, len(questions)), 10)
    q_lists = []
    for num in results:
        q_lists.append(questions[num])
    temp = []
    for q in q_lists:
        temp.append(q.to_json())
    # print(temp)
    truth = []
    for t in temp:
        # print(t['right_answer'])
        truth.append(list(t.values())[t['right_answer'] + 1])
    session[TRUTH] = truth
    return jsonify(temp)


# 答题结果，计算用户答案_ajax_post，无csrf保护
# @csrf.exempt
@bp.route('/result/', methods=['POST'])
def result():
    if request.method == 'POST':
        try:
            record = Answer_record.query.filter_by(user_id=g.user.id).order_by(
                Answer_record.start_time.desc()).first()
            record.submit_time = datetime.datetime.now()
            db.session.commit()
            post_data = request.get_json()
            data = post_data.get('selected')
            selected = []
            for value in data.values():
                selected.append(value)
            session[SELECTED] = selected
            message = {'status': 'success'}
        except Exception as e:
            traceback.print_exc()
            return jsonify({'status': 'fail'})

        else:
            return jsonify(message)


# 告知分数，抽奖
@bp.route('/score/')
@login_required
def score():
    return render_template('front/score.html')


# 积分api_ajax_get
@bp.route('/score_api/')
def score_api():
    # 默认总分为0，默认未获奖,默认安全积分未0
    # 默认不抽奖
    raffle = False
    score = 0
    award = False
    integral = 0
    print(g.selected)
    for index, value in enumerate(g.selected):
        if g.truth[index] == value:
            score += 10
    record = Answer_record.query.filter_by(user_id=g.user.id).order_by(
        Answer_record.start_time.desc()).first()
    # 如果日期在6月5日8:30-22:00之间则抽奖
    if datetime.datetime.strptime(START_TIME,
                                  '%Y-%m-%d %H:%M:%S') <= record.submit_time <= datetime.datetime.strptime(
        END_TIME, '%Y-%m-%d %H:%M:%S'):
        raffle = True
    # 如果在300秒之内答完题则获奖而且今天首次答题=100分
    today_submit_nums = len(Answer_record.query.filter_by(user_id=g.user.id).all())
    if (record.submit_time - record.start_time).seconds <= TIME_LIMIT and today_submit_nums == 1 and score == 100:
        award = True
        # 积分抽奖
        integral_list = [0.5] * 85 + [1] * 10 + [2] * 5
        index = random.randint(0, len(integral_list) - 1)
        integral = integral_list[index]
    # 保存分数到数据库
    record.score = score
    record.integral = integral
    db.session.commit()
    return jsonify(score=score, raffle=raffle, award=award, integral=integral)
