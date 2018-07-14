import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123'
    CSRF_ENABLED = True