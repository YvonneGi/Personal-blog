from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('Post Your Blog')
    body = TextAreaField('Body', validators=[Required()])
    submit = SubmitField('Submit Post')


class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()


class SubscriptionForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    submit = SubmitField()

class UpdatePost(FlaskForm):
    body = TextAreaField("Update Post", validators=[Required()])
    submit = SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
