from flask import Flask, redirect, url_for, render_template
from flask import request
import sqlite3
from task_sqlite import Connection

app = Flask(__name__)

db_connection = Connection(
    sqlite3.connect('tasks.db', check_same_thread=False)
    )

@app.route("/") # "/" is Home page - Can also do /home.
def home():
    return "<h1>SELECTED TASKS<h1>"

@app.route("/tasks")
def tasks():
    return render_template('tasks.html', variable = db_connection.view_tasks())

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()