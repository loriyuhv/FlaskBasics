import datetime
from datetime import timedelta


class Config(object):
    DEBUG = True
    SECRET_KEY = "umsuladsdflaskjdf"
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=20)


class ProductionConfig(Config):
    pass
    # DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    pass
    # DEBUG = True


class TestingConfig(Config):
    pass
    # TESTING = True
