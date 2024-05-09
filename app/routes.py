"""Routes"""
from flask import (Blueprint, render_template)

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def main():
    """Index"""
    return render_template('main.html')
