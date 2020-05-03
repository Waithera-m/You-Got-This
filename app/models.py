from . import db

class User(db.Model):

    '''
    class faciliates the creation of user objects
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {user.username}'

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