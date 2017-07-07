from app import app
from flask import render_template, redirect

@app.route('/')
@app.route('/ask')
def ask():
    

