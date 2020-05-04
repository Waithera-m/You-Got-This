from flask import render_template,redirect,url_for,abort,request
from . import main
from ..models import User,Pitch
from .forms import EditProfile,PitchForm
from .. import db,photos
from flask_login import login_required,current_user


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

@main.route('/user/<uname>/update', methods=["GET","POST"])
@login_required
def edit_profile(uname):

    '''
    view function renders edit profile template
    '''
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    
    form = EditProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/edit.html',form=form)

@main.route('/user/<uname>/update/pic', methods=["POST"])
@login_required
def update_pic(uname):

    '''
    view function facilitates the processing of form submission request
    '''
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_photo_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new',methods=["GET","POST"])
@login_required
def new_pitch():

    '''
    function renders new_pitch template and form that users can use to create new pitch
    '''
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.pitch.data
        category = pitch_form.category.data

        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,likes=0,dislikes=0,user=current_user)

        new_pitch.save_pitch()
        return redirect(url_for("main.index"))
    
    title="New Pitch"
    return render_template('new_pitch.html',title=title,pitch_form=pitch_form)