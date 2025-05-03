from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about/discoverus')
def discoverus():
    return render_template('discover_us.html')

@app.route('/about/executive')
def executive_team():
    return render_template('executive_team.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form data here
        name = request.form.get('name')
        message = request.form.get('message')
        # Save to DB (to be implemented)
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
