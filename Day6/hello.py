from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Email, DataRequired
from flask_mail import Mail, Message

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'this is a secrete key for flask_form'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PROT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='cheng.yi.lin.217@gmail.com',
    MAIL_PASSWORD='ji3g45/4u6',
    MAIL_DEFAULT_SENDER='cheng.yi.lin.217@gmail.com'
)
mail = Mail(app)


class Comment(FlaskForm):
    email = StringField(label='Your Email : ', validators=[Email()])
    subject = StringField(label='Subject', validators=[DataRequired()])
    content = TextAreaField(label='Content', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


@app.route('/', methods=["GET", "POST"])
def index():
    form = Comment()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['subject'] = form.subject.data
        session['content'] = form.content.data
        msg_recipients = form.email.data
        msg_subject = form.subject.data
        msg_content = form.content.data
        msg = Message(subject=msg_subject, recipients=[msg_recipients], body=msg_content)
        mail.send(msg)
        return redirect(url_for('index'))
    return render_template("email.html",
                           form=form,
                           email=session.get('email'),
                           subject=session.get('subject'),
                           content=session.get('content'))
