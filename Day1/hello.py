from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world</h1>'

@app.route('/usr/<name>')
def user_name(name):
    return f'<h1>Hello, {name}</h1>'