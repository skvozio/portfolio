from flask import Flask, render_template, request, redirect
from flask_mail import Mail
from flask_mail import Message  
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT') or 25)
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') is not None
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == "POST":
        data = request.form.to_dict()
        msg = Message("New message from your Portfolio website", 
                       sender="maksim.buturlakin@gmail.com",
                       recipients=["maksim.buturlakin@gmail.com",])
        msg.body=data['name'] + ' wrote to you: \n' + data['message'] + \
        '\nEMAIL WAS ' + data['email']
        mail.send(msg)
        return redirect('/')
    else:
        return 'Something went wrong'
