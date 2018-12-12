from . import user
from flask import render_template


@user.route('/')
def index():
    return render_template('index.html')