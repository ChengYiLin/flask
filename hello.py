from flask import Flask, render_template
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

@app.route('/', methods=["GET", "POST"])
def index():
    name = None
    form = first_form()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("index.html", form=form, name=name)