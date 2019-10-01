from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm): #Creating Registration form class
    email = StringField('Your Email Address',validators=[Required(),Email()]) #input field email passing in required and email validators 
    username = StringField('Username',validators=[Required()]) #input username field
    password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message="Passwords must match")]) #input password field
    password_confirm = PasswordField('Confirm Passwords',validators=[Required()]) #input password confirm field
    submit = SubmitField('Sign Up')

#Login Input Fields 
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    #input fields for the users email,password and a boolean to confirm whether the user wants to be logged out after the session
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
 
