from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ----------- DATABASE SETUP (One Time Only) -----------

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    ''')

    conn.commit()
    conn.close()

# ----------- ROUTES -----------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()

    return f"Stored: {username} and {password}"

# ----------- RUN APP -----------

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
