class Config(object):

    SECRET_KEY = 'pianalytix'
    MY_NEW_VAR = 'added via browser github'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
