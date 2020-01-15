import os
from flask import Flask,redirect,render_template,request,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html',title='About')


if __name__ == "__main__":
    app.run(debug=True)