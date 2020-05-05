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

@main.route('/pitches/business')
def business():

    '''
    view function returns business.html and its contents
    '''
    business_pitches = Pitch.get_pitches('business')

    return render_template("business.html",business_pitches=business_pitches)

@main.route('/pitches/poverty')
def poverty():

    '''
    view function returns poverty.html and its contents
    '''
    poverty_pitches = Pitch.get_pitches('poverty')
    
    return render_template("poverty.html",poverty_pitches=poverty_pitches)

@main.route('/pitches/love')
def love():

    '''
    view function returns love template and its contents
    '''
    love_pitches = Pitch.get_pitches('love')

    return render_template("love.html",love_pitches=love_pitches)

@main.route('/pitches/humanity')
def humanity():

    '''
    view function returns humanity template and its contents
    '''
    humanity_pitches = Pitch.get_pitches('humanity')
    

    return render_template("humanity.html",humanity_pitches=humanity_pitches)


@main.route('/pitch/<int:id>',methods=["GET","POST"])
def pitch(id):

    '''
    view function returns single pithc
    '''
    pitch = Pitch.get_pitch(id)
    
    pitch_id = pitch.id
    
    
    if request.args.get("like"):
        pitch.likes = pitch.likes +  1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    return render_template("pitch.html",pitch=pitch)

@main.route('/user/<uname>/pitches')
def registered_pitches(uname):
     
    

    '''
    view function returns pitches submitted by a specific user
    '''
    
    user = User.query.filter_by(username=uname).first()
    
    pitches = Pitch.query.filter_by(user_id=user.id).all()
   

    return render_template("profile/pitches.html",user=user,pitches=pitches)


