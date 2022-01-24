import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN') or '123'
