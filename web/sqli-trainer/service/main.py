from flask import Flask, request, jsonify, redirect, url_for, flash, session, send_file
import sqlite3
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

def check_login(username, password):
    sqlite3.enable_callback_tracebacks(True)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # Setup database
    cursor.execute("create table users (name text, pass text)")
    cursor.execute(f"insert into users values ('user', '{secrets.token_hex(16)}')")

    # Execute query
    query = f"SELECT name FROM users WHERE name = '{username}' AND pass = '{password}'"
    result = cursor.execute(query).fetchall()
    conn.close()
    if len(result) != 1:
        return result, "Login failed!"
    elif result[0][0] != "admin":
        return result, "Only the admin can have the flag!"
    return result, "grey{SQLi_1s_st1ll_rel3v4nt_1n_2024}"

@app.route('/')
def index():
    return send_file("static/index.html")

@app.route('/login', methods=['POST'])
def login():
    message=""
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # Vulnerable SQL query
    try:
        result, flag = check_login(username, password)
    except Exception as e:
        return jsonify({"err": str(e)})
    return jsonify({"flag": flag, "res": result})