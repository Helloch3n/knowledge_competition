from flask_migrate import Migrate
from exts import db
from main import create_app
# from apps.models import User
# from apps.models import Question

app = create_app()

Migrate(app, db)
