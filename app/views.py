from flask import render_template
from app import app 


# views

@app.route('/')
def index():

    '''
    view rooy page function that returns the index page and its data

    '''
    return render_template ('index.html')
    