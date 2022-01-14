from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap


import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"

Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
