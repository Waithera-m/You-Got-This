from flask import render_template
from . import main


@main.route('/')
def index():

    '''
    View function renders index.html, the landing page
    '''
    title = 'You Got This'

    return render_template('index.html',title=title)