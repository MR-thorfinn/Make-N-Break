from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    return f"Received: {username} and {password}"

if __name__ == '__main__':
    app.run(debug=True)
