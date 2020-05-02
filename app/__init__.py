from flask_bootstrap import Bootstrap
from flask import Flask
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):

    '''
    Function facilitates app, configuration, and extensions' initialization
    '''

    app = Flask(__name__)

    #create app configurations
    app.config.from_object(config_options[config_name])

    #initialize extensions
    bootstrap.init_app(app)

    #initialize blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app