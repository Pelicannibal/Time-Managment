from flask import Flask, redirect, url_for
from flask import request

app = Flask(__name__)

@app.route("/") # "/" is Home page - Can also do /home.
def home():
    return "Hello! <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()