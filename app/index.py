import functools

from flask import (
    Blueprint, flash,render_template, request, url_for
)

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def root():
    return render_template('home.html')