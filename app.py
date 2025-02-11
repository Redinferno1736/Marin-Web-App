import requests
from flask import Flask, flash, redirect, render_template, request, session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

with get_db_connection() as conn:
    db = conn.cursor()
    db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            username TEXT NOT NULL, 
            hash TEXT NOT NULL)
    """)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if password != confirm:
            flash("Passwords do not match!")
            return render_template("register.html")

        hash = generate_password_hash(password)

        try:
            with get_db_connection() as conn:
                db = conn.cursor()
                db.execute("INSERT INTO users (username, hash,LeetUsername) VALUES (?, ?,?)", (username, hash,"1"))
                conn.commit()
            return redirect('/login')
        except sqlite3.IntegrityError as e:
            flash("Username has already been registered!")
            return render_template("register.html")

    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username and password cannot be empty!")
            return render_template("login.html")

        with get_db_connection() as conn:
            db = conn.cursor()
            db.execute("SELECT * FROM users WHERE username = ?", (username,))
            rows = db.fetchall()

        if len(rows) != 1:
            flash("Invalid username or username not found!")
            return render_template("login.html")

        if not check_password_hash(rows[0]["hash"], password):
            flash("Invalid password!")
            return render_template("login.html")

        session["user_id"] = rows[0]["id"]
        return redirect("/data")
    return render_template("login.html")


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/")