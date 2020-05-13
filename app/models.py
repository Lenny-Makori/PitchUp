from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email =db.Column(db.String(255),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch=db.relationship('Pitch',backref='col',lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    comments=db.relationship('Comment',backref='user',lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
       return check_password_hash(self.pass_secure,password)

    @classmethod
    def get_user(cls,id):
        user= User.query.filter_by(id=id).first()
        return user

    def __repr__(self):
            return f'User {self.username}'

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    __tablename__='pitch'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    category=db.Column(db.String)
    description=db.Column(db.String)
    # time_posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comment=db.relationship('Comment',backref='comment',lazy='dynamic')
    
    
    def __repr__(self):
        return f'User {self.pitch}'

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pitch(cls,id):
        pitch= Pitch.query.filter_by(user_id=id).all()
        return pitch
    @classmethod
    def get_pitch_id(cls,id):
        pitch= Pitch.query.filter_by(id=id).all()
        return pitch
# ******88RETURNS ALL PITCHES
    def get_all_pitch():
        pitch= Pitch.query.all()
        return pitch
    @classmethod
    def get_all_pitchs():
        pitch= Pitch.query.first()
        return pitch
    @classmethod
# Getting categories
    def get_pitch_category(cls,category):
        pitch= Pitch.query.filter_by(category=category).all()
        return pitch
class Comment(db.Model):
    __tablename__='comment'

    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String)
    upvote=db.Column(db.Integer)
    downvote=db.Column(db.Integer)
    time_posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitch.id"))
    # pitchcategory=db.relationship("Pitch",backref="category",lazy="dynamic")

   
    def save_new_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comment = Comment.query.filter_by(pitch_id=id).all()
        return reviews
    

    
   