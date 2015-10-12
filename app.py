from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', post = 8000)
