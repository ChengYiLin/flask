from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a key'

class first_form(FlaskForm):
    name = StringField(label='What is your name', validators=[DataRequired()])
    submit = SubmitField('Submit')

