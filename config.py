import os

class Config:

    '''
    Class facilitates the creation of config objects
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class DevConfig(Config):

    '''
    Class inherits general configurations from Config class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mary:pixie01@localhost/pitches'

    DEBUG = True

class ProdConfig(Config):

    '''
    Class inherits general configurations from Config class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):

    '''
    Class inherits general configurations from Config class  and facilitates the testing of class and database behavior
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mary:pixie01@localhost/pitches_test'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}