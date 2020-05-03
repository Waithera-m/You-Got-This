from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required
from ..models import User

class EditProfile(FlaskForm):

    '''
    class facilitates the creation of profile objects
    '''
    bio = TextAreaField('Let the world know more about you',validators=[Required()])
    submit = SubmitField('Add Bio')