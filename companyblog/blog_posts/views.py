# blog_post/views.py
from flask import render_template, redirect, request, url_for, Blueprint, flash
from flask_login import login_user, current_user, logout_user, login_required

from companyblog import db
from companyblog.models import BlogPost
from companyblog.blog_posts.forms import BlogPostForm


blog_posts = Blueprint('blog_posts',__name__)

# CREATE

# BLOG POST VIEW
# UPDATE