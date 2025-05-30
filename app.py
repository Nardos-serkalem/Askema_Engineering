from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import User



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/partnership')
def partnership():
    return render_template('partnership.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/team')
def team():
    return render_template('team.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
