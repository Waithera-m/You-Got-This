import os

class Config:

    '''
    Class facilitates the creation of config objects
    '''
    pass

class DevConfig:

    '''
    Class inherits general configurations from Config class
    '''

    DEBUG = True

class ProdConfig:

    '''
    Class inherits general configurations from Config class
    '''
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}