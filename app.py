from flask import Flask, render_template

app = Flask(__name__)

# Home page (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Authentication pages
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# Other main pages
@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/partnership')
def partnership():
    return render_template('partnership.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# About and its subpages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about/discover')
def discover_us():
    return render_template('discover_us.html')

@app.route('/about/team')
def executive_team():
    return render_template('executive_team.html')


if __name__ == '__main__':
    app.run(debug=True)
