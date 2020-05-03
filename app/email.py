from flask_mail import Message
from flask import render_template
from . import mail

subject_pref = 'You Got This'
sender_email = 'watchlist.flask@gmail.com'

def email_message(subject,template,to,**kwargs):

    '''
    function defines the key components of the welome email
    '''
    email = Message(subject_pref+subject,sender=sender_email,recipients=[to])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
    