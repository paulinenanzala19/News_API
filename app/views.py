from flask import render_template
from app import News



@News.route('/')
def index():
    return render_template('index.html')