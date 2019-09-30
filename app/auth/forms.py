from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm): 
    email = StringField('Your Email Address',validators=[Required(),Email()]) 
    username = StringField('Username',validators=[Required()]) 
    password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message="Passwords must match")]) 
    password_confirm = PasswordField('Confirm Passwords',validators=[Required()]) 
    submit = SubmitField('Sign Up')

 
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')