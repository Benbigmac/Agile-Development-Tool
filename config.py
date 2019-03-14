import os

class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
        SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://firescrum:admin@SEW-DESK[:3306]/Firescrum'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
