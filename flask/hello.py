from flask import Flask, render_template, session, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from database import db, User 
from flask_sqlalchemy import SQLAlchemy
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
bootstrap = Bootstrap(app)
# SQLAlchemy 初始化
db = SQLAlchemy(app)
db.init_app(app)
# Flask-Migrate 初始化
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# 設定我們的 Form 的 Key 
app.config['SECRET_KEY'] = 'this is a key'
# 設定 SQLAlchemy 參數
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

class the_form(FlaskForm):
    name = StringField(label='What is your name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=["GET", "POST"])
def index():
    form = the_form()
    if form.validate_on_submit():
        # 搜尋我們 database 有沒有這名字，沒有加資料庫，有的話就有
        # 用 session 變數來儲存變數，這樣才記得住
        # 最後記得清空資料，不然 redirect 之後還是在那邊
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known']=False
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''

        return redirect(url_for('index'))
    return render_template('index.html', form=form,name=session.get('name'), known=session.get('known', False))