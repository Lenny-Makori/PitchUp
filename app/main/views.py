from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,Comment

from flask_login import login_required,current_user
from ..models import User
from  ..import db,photos
from .forms import UpdateProfile,AddPitch,CommentInput
from datetime import datetime


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message='Index Page'
    title = 'Home - Welcome to The Pitchpitches'
    # user=User.get_user(id)
    
    return render_template('index.html',title=title,message=message)


# @main.route('/user/<uname>')
# def profile(uname):
    

#     user = User.query.filter_by(username = uname).first()
#     user_id=user.id
#     pitches=Pitch.get_pitch(user_id)
    
    
#     if user is None:
#         abort(404)

#     return render_template("profile/profile.html", user = user,pitches=pitches)



# @main.route('/pitch/<category>')
# def pitch(category):

    
   
#     all_pitches=Pitch.query.filter_by(category=category).all()
#     pitch=Pitch.query.filter_by(category=category).first()

#     pitches=Pitch.get_pitch_category(category)
#     form=CommentInput()
    
#     if form.validate_on_submit():
#         description=form.description.data
        
#         new_comment=Comment(description=description,upvote=0,downvote=0,pitch_id=pitchess.id)
#         # SAVE COMENT
#         new_comment.save_new_comment()
#         return redirect(url_for('.pitch',category=pitches.category))

#         # return redirect(url_for('.movie',id = movie.id ))
#     #
#     pitches=Pitch.get_pitch_category(category)

#     return render_template('categories.html',category = category,all_pitches=all_pitches,form=form)


# @main.route('/user/pitch/<id>', methods = ['GET','POST'])
# @login_required
# def new_pitch(id):  
#     pitch_form=AddPitch()
#     user=User.get_user(id)
#     if form.validate_on_submit():
#         title=pitch_form.title.data
#         category=pitch_form.category.data
#         description=pitch_form.description.data
#         new_pitch=Pitch(title=title,category=category,description=description,user_id=user.id)

#         new_pitch.save_pitch()
#         return redirect(url_for('.index',id=user.id))
#     title='New Pitch'
#     return render_template('pitches.html',title = title, pitch_form=pitch_form,user=user)


# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))

#     return render_template('profile/update.html',form =form)





