from flask import render_template,redirect,url_for,abort
from . import main
from ..models import User


@main.route('/')
def index():

    '''
    View function renders index.html, the landing page
    '''
    title = 'You Got This'

    return render_template('index.html',title=title)

@main.route('/user/<uname>')
def profile(uname):

    '''
    view function renders user's profile page
    '''
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html",user=user)