import os
import sqlite3
from flask import Flask, render_template, request

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATES_DIR)

def get_db_connection():
    conn = sqlite3.connect(os.path.join(BASE_DIR, "users.db"))
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "OWASP Mini Project - SQL Injection Demo"

@app.route("/login_vuln", methods=["GET", "POST"])
def login_vuln():
    if request.method == "GET":
        return render_template("login_vuln.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        # استعلام ضعيف قابل لـ SQL Injection
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Executing:", query)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query)
        user = cur.fetchone()
        conn.close()

        if user:
            return f"Bienvenue {user['username']} (LOGIN VULNÉRABLE RÉUSSI)"
        else:
            return "Invalid credentials (toujours vulnérable à SQL Injection)"

if __name__ == "__main__":
    app.run(debug=True)
