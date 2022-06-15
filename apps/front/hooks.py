import config
from flask import session, g
from ..models import User
from .views import bp


@bp.before_request
def before_request():
    # 保存用户信息到g
    if config.FRONT_USER_ID in session:
        user_dl_id = session.get(config.FRONT_USER_ID)
        user = User.query.filter_by(dl_id=user_dl_id).first()
        if user:
            g.user = user
    # 保存正确答案到g
    if config.TRUTH in session:
        truth = session.get(config.TRUTH)
        g.truth = truth
    # 保存答题者选项到g
    if config.SELECTED in session:
        selected = session.get(config.SELECTED)
        g.selected = selected
