from flask import render_template
from . import auth

@auth.route('/login')
def login():

    '''
    view function renders login.html
    '''
    return render_template('auth/login.html')