import smtplib
import email.message
from models.req_model import Req
from flask import render_template 

def enviar_email(r:Req):  
    corpo_email = None

    if(r.category == "account deletion"):
        corpo_email = render_template('account_deletion_template.html', user=r.user)

    elif(r.category == "full storage"):
        corpo_email = render_template('full_storage_template.html', user=r.user)
    
    elif(r.category == "plan promotion"):
        corpo_email = render_template('plan_promotion_template.html', user=r.user)
    
    elif(r.category == "register confirmation"):
        corpo_email = render_template('registration_confirmation.html', user=r.user)
    
    else:
        raise Exception("a categoria nao existe") 

    msg = email.message.Message()
    msg['Subject'] = r.category
    msg['From'] = 'remetente'
    msg['To'] = r.user.email
    password = 'senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')