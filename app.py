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
        f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return "Login Successful!"
    else:
        return "Login Failed!"

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    )

    conn.commit()
    conn.close()

    return "Registered Successfully!"

# ----------- RUN APP -----------

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
