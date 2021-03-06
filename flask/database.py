from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# 顯示我們目前檔案的路徑
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 設定我們的環境參數 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 初始化
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username