from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):

    '''
    function retrieves a user with a given id
    '''
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):

    '''
    class faciliates the creation of user objects
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)
    username = db.Column(db.String(255),index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    
    @property
    def password(self):

        '''
        function blocks access to password property
        '''
        raise AttributeError('Password attribute cannot be read')

    @password.setter
    def password(self,password):

        '''
        function generates password hash
        '''
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self,password):

        '''
        function checks if entered and hashed passwords match
        '''
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):

    '''
    class facilitates the creation of role objects
    '''
    __tablename__='roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'