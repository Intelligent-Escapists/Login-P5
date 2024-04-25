import redis

class Applicationconfig:
    SECRET_KEY = 'dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lab:Developer123!@localhost:3306/mercaditApp'