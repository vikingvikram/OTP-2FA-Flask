from flask import Flask, render_template, request, redirect
import sqlite3
import pyotp
import qrcode
import os

app = Flask(__name__)
DB = "users.db"

# -------------------- DB SETUP --------------------
def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            secret TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -------------------- REGISTER --------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        secret = pyotp.random_base32()

        # Save to DB
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password, secret))
        conn.commit()
        conn.close()

        # Generate QR
        uri = pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name="VikramAuth")
        img = qrcode.make(uri)
        img.save(f"static/qrcodes/{username}.png")

        return render_template("register.html", qr=f"static/qrcodes/{username}.png")

    return render_template("register.html", qr=None)

# -------------------- LOGIN --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        conn.close()

        if user and user[1] == password:
            return redirect(f"/verify?u={username}")
        else:
            return "Invalid credentials!"

    return render_template("login.html")

# -------------------- VERIFY OTP --------------------
@app.route("/verify", methods=["GET", "POST"])
def verify():
    username = request.args.get("u")

    if request.method == "POST":
        otp = request.form["otp"]

        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("SELECT secret FROM users WHERE username=?", (username,))
        secret = cur.fetchone()[0]
        conn.close()

        totp = pyotp.TOTP(secret)

        if totp.verify(otp):
            return redirect("/dashboard")
        else:
            return "Invalid OTP!"

    return render_template("verify.html", username=username)

# -------------------- DASHBOARD --------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

app.run(debug=True)
