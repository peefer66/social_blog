from flask import render_template, redirect, request, url_for, Blueprint, flash
from flask_login import login_user, current_user, logout_user, login_required

from companyblog import db
from companyblog.models import User, BlogPost
from companyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from companyblog.users.picture_handler import add_profile_pic

########################################
# ######################################
# REGISTER
# LOGIN
# UPDATE PROFILE
# LOGOUT
# USER LIST OF BLOG POSTS
########################################
########################################

# Create Blueprint => register in company/__init__.py
users = Blueprint('users', __name__)

# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index')) # core.index Blueprint

# Register
@users.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.commit()
        flash('Thank you for registering')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

# Login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_pasword(form.password.data) and user is not None:
            login_user(user) 
            flash('You successfully logged in')
            
            # if user has been redirected from another page 
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('/')
                redirect(next)
    return render_template('login.html', form=form)

    


