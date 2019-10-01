from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from flask_login import UserMixin,login_required
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String)
    password = db.Column(db.Integer)
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    posts = db.relationship('Post', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'post', lazy = "dynamic")

    all_posts = []
    
    def __init__(self,title,body):
        self.title = title
        self.body = body
        

    def save_post(self):
        '''
        Save posts
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_posts(cls):
        Post.all_posts.clear()

    
    def get_posts(id):
        posts = Post.query.filter_by(title_id=id).all()
        return posts

    def delete_post(self):
        '''delete a given post from the database'''
        db.session.delete(self)
        db.session.commit()



class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
  

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments=Comment.query.filter_by(post_id=id).all()
        return comments
    

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

class Subscription(db.Model):

    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    

class Quote:

    def __init__(self,id,author,content):
        self.id=id
        self.author=author
        self.content=content
        

    
