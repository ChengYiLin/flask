from flask import Flask, render_template

app = Flask(__name__)

mydict = {'key':98}
mylist = ['a', 'b', 'c', 'd']
class Animal():
    def __init__(self, name):
        self.name = name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/variable')
def variable():
    return render_template('variable.html', mydict=mydict, mylist=mylist, myobj=Animal('dog'))

@app.route('/block')
def block():
    return render_template('extend.html')