activate_this = 'F:/Desktop/P_P/knowledge_competition/venv/Scripts/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys

sys.path.insert(0, 'F:/Desktop/P_P/knowledge_competition')

from flasky import app as application

# from main import create_app
#
# application = create_app()
