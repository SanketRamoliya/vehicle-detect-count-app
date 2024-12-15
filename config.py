class Config(object):

    SECRET_KEY = 'pianalytix'
    MY_NEW_VAR = 'added via browser github add by ansh by sanket 645PM'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
