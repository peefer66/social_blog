#USERS/FORM.PY

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user

from companyblog.models import User

###################################################
################ LOGIN FORM #######################
###################################################

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

###################################################
################ REGISTRATION FORM ################
###################################################

class RegistrationForm(FlaskForm):
    # Registration fioelds
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4, max=25)])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired(),
                                EqualTo(password,
                                message='Password must match')])
    submit = SubmitField('Register')

    def check_email(self,field):
        # Check if email already registered
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This Email has already been registered')
    
    def check_username(self,field):
        # Check if username is already registered
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username has already been registered')


class UpdateUserForm(FlaskForm):
    # Update user info
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        # Check if email already registered
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This Email has already been registered')
    
    def check_username(self,field):
        # Check if username is already registered
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username has already been registered')





