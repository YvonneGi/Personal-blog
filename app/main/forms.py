from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required

#Post Form
class PostForm(FlaskForm):
    title = StringField('Post Your Blog')
    body = TextAreaField('Body', validators=[Required()])
    submit = SubmitField('Submit Post')

#Comment Form
class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()

#Subscription Form
class SubscriptionForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    submit = SubmitField()

    # def validate_email(self,field):
    #     if SubscriptionForm.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email exists')

class UpdatePost(FlaskForm):
    body = TextAreaField("Update Post", validators=[Required()])
    submit = SubmitField('Post')
