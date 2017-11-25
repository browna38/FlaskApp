from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
user = {'nickname': 'Michael'}  # Not a real user
return render_template('index.html',
title='Home',
user=user)
