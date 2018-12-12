from . import login
from info.models import User
from flask import render_template

# @login.route('/register')
# def register():
#     pass

@login.route('/')
def userinfo():
    user = User.query.filter(User.is_admin==True).first()
    return render_template('index.html',data=user)