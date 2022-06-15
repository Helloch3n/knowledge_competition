from flask import Flask, request, jsonify
import config
from exts import db, csrf
from apps.front import bp as front_bp
from apps.cms import bp as cms_bp
from flask_cors import CORS
import traceback


def create_app():
    app = Flask(__name__)
    # 跨域访问
    CORS(app, resources={r'/*': {'origins': '*'}})
    # 改变jinja2模板
    app.jinja_env.variable_start_string = '{['
    app.jinja_env.variable_end_string = ']}'
    app.config.from_object(config)

    db.init_app(app)
    # csrf保护
    csrf.init_app(app)

    app.register_blueprint(front_bp)
    app.register_blueprint(cms_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080)
