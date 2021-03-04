class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = "sqlite://:memory:"


class DevelopmentConfig(Config):
    ENV = "development"
    SECRET_KEY = "simple_api_test=DevelopmentConfig"
    DEBUG = False


class TestingConfig(Config):
    ENV = "testing"
    SECRET_KEY = "simple_api_test=TestingConfig"
    TESTING = True
    DEBUG = True
