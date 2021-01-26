from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail
from flask_mail import Message  
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT') or 25)
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL') is not None
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'Super-Secret-Super-Key-123'

mail = Mail(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == "POST":
        data = request.form.to_dict()
        title = "New message from your Portfolio website"
        name = data.get('name') or 'Anonymous'
        email = data.get('email')
        message = data.get('message') or "Message was empty"
        msg = Message(title, 
                       sender="buturlakin.portfolio@yandex.ru",
                       recipients=["maksim.buturlakin@gmail.com",])
        msg.body = name + ' wrote to you: \n' + message + \
        '\nemail was ' + email
        mail.send(msg)
        flash('Your message was sent!')
        return redirect(url_for('index'))
    else:
        return 'Something went wrong'
