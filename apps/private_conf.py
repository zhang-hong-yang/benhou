import os

DEBUG = True

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'benhou.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
