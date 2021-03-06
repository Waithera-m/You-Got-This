from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import UserRegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import email_message


@auth.route('/login', methods=["GET","POST"])
def login():

    '''
    view function renders login.html
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.index'))
        
        flash('Invalid email or password')
    
    title = "You Got This Login"

    return render_template('auth/login.html',login_form=login_form,title=title)

@auth.route('/logout')
@login_required
def logout():

    '''
    view function logs out an authenticated user
    '''
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/register',methods=["GET","POST"])
def register ():

    '''
    view function renders registration form
    '''
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        email_message("Welcome to You Got This","email/welcome_user",user.email,user=user)
        return redirect(url_for('.login'))
        title="New Account"
    return render_template('auth/register.html',registration_form=form)
