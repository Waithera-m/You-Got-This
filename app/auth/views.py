from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .forms import UserRegistrationForm
from .. import db

@auth.route('/login', methods=["GET","POST"])
def login():

    '''
    view function renders login.html
    '''
    return render_template('auth/login.html')

@auth.route('/register',methods=["GET","POST"])
def register ():

    '''
    view function renders registration form
    '''
    form = UserRegistrationForm()
    if form.validate_on_submit():
        User = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(urls_for('.login'))
        title="New Account"
    return render_template('auth/register.html',registration_form=form)
