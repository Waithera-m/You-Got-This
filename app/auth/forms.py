from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class UserRegistrationForm(FlaskForm):

    '''
    class facilitates the creation of form input fields
    '''
    email = StringField('Enter your email address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Enter your password',validators=[Required(),EqualTo('password_confirm',message = 'Both passwords must match')])
    password_confirm = PasswordField('Confirm your password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):

        '''
        function checks if email is already in the database and if it is, it raises a ValidationError
        '''
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('The email already exists')

    def validate_username(self,data_field):

        '''
        function checks if there is an account that uses the entered username and if there is, it raises a ValidationError
        '''
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('The username already exists')

class LoginForm(FlaskForm):

    '''
    class facilitates the creation of a login form
    '''
    email = StringField('Enter your email address',validators=[Required()])
    password = PasswordField('Enter your password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')