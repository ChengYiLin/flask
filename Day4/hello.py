from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'this is a key'

class first_form(FlaskForm):
    name = StringField(label='What is your name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# @app.route('/', methods=["GET", "POST"])
# def index():
#     name = None
#     form = first_form()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template("index.html", form=form, name=name)

# @app.route('/jinja2', methods=["GET", "POST"])
# def jinja2():
#     form = first_form()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     else:
#         return render_template("jinja2.html", form=form)

@app.route('/', methods=['GET','POST'])
def index():
    form = first_form()
    if form.validate_on_submit():
        oldname = session.get('name')
        if oldname is None or oldname == form.name.data: 
            session['state'] = False
            flash("The name has been used again !")
        else:
            session['state'] = True
            flash("Successfully change your name")
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template("index.html", form=form, name=session.get('name'), state=session.get('state'))
