import os

class Config:

    '''
    Class facilitates the creation of config objects
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mary:pixie01@localhost/pitches'

class DevConfig(Config):

    '''
    Class inherits general configurations from Config class
    '''

    DEBUG = True

class ProdConfig(Config):

    '''
    Class inherits general configurations from Config class
    '''
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}