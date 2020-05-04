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

class PitchForm(FlaskForm):

    '''
    class facilitates the creation of pitch form objects
    '''
    title = StringField('Pitch Title',validators=[Required()])
    pitch = TextAreaField('Tell us more about your pitch',validators=[Required()])
    category = TextAreaField('Indicate the category that best suits your pitch',validators=[Required()])
    submit = SubmitField('Share Pitch')