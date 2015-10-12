from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/@<username>')
def profile():
	return render_template('profile.html')

@app.route('/@<username>/<post>')
def read():
	return render_template('post.html')

@app.route('/@<username>/<post>/comments', methods=['POST'])
def comment():
	return 'Coming Soon';

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('new.html')

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', post = 8000)
