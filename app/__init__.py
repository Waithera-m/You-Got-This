from flask_bootstrap import Bootstrap
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
photos = UploadSet('photos',IMAGES)
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
#set name of log in view
login_manager.login_view = 'auth.login'

db = SQLAlchemy()

bootstrap = Bootstrap()

def create_app(config_name):

    '''
    Function facilitates app, configuration, and extensions' initialization
    '''

    app = Flask(__name__)

    #create app configurations
    app.config.from_object(config_options[config_name])

    configure_uploads(app,photos)

    #initialize extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    #initialize blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    return app
