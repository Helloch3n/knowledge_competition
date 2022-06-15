import os

DB_USERNAME = 'root'
DB_PASSWORD = 'lrc123456'
DB_HOST = 'localhost'
DB_NAME = 'knowledge_competition'
DB_PORT = '3306'
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4".format(username=DB_USERNAME,
                                                                                               password=DB_PASSWORD,
                                                                                               host=DB_HOST,
                                                                                               dbname=DB_NAME,
                                                                                               port=DB_PORT)

#sqlserver
# DB_USERNAME = 'lrc'
# DB_PASSWORD = 'Helloch3nl0ve'
# DB_HOST = '10.40.10.23'
# DB_NAME = 'knowledge_competition'
#
# DB_URI = "mssql+pymssql://{username}:{password}@{host}/{dbname}".format(username=DB_USERNAME, password=DB_PASSWORD,
#                                                                         host=DB_HOST, dbname=DB_NAME)


# 设置SQLALCHEMY_URI
SQLALCHEMY_DATABASE_URI = DB_URI
# 忽略SQLALCHEMY_TRACK_MODIFICATIONS报错
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 设置csrf密钥
SECRET_KEY = os.urandom(24)

# 设置cokkie id
FRONT_USER_ID = 'FRONT_USER_ID'

SELECTED = 'SELECTED'

TRUTH = 'TRUTH'

# 设置答题时间限制
TIME_LIMIT = 300

# 抽奖开始时间
START_TIME = '2022-06-05 08:30:00'
END_TIME = '2022-06-05 22:00:00'

# 设置ip和端口
# SERVER_NAME = '192.168.160.1:8080'

# 每天答题次数
SUBMIT_LIMIT = 3

# debug模式
DEBUG = False
