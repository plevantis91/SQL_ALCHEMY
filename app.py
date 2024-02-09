from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)

def app_context():
    with app.app_context():
        yield


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'

db = SQLAlchemy()
db.app = app

db.init_app(app)

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')
