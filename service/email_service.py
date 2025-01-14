from flask import render_template 
from models.req_model import Req
from dotenv import load_dotenv
import smtplib
import email.message
import os
import logging

#configuração dos logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#Dados do .env
load_dotenv()
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
email_bot = os.getenv('EMAIL_BOT')
pass_bot = os.getenv('PASSWORD_BOT')

if not email_bot or not pass_bot:
    raise EnvironmentError("EMAIL_BOT ou PASSWORD_BOT não foram configurados corretamente no arquivo .env")

#func pra pegar a conexão
def get_smtp_connection():
    s = smtplib.SMTP(f'{smtp_server}: {smtp_port}')
    s.starttls()
    return s


#func pra verificar se a categoria existe e se existir, qual template de email enviar
def verify_category(r:Req):
    
    templates = {
        "account deletion": 'account_deletion_template.html',
        "full storage": 'full_storage_template.html',
        "plan promotion": 'plan_promotion_template.html',
        "register confirmation": 'registration_confirmation.html'
    }
    
    if r.category not in templates:
        logger.error(f"categoria {r.category} não existe")
        raise Exception(f"a categoria {r.category} nao existe") 
    
    return render_template(templates[r.category], user=r.user.__dict__) 
    

def enviar_email(r:Req): 
    #template do email 
    corpo_email = verify_category(r)


    msg = email.message.Message()
    #categoria da msg
    msg['Subject'] = r.category
    #remetente
    msg['From'] = email_bot
    #destinatário
    msg['To'] = r.user.email
    #senha do remetente
    password = pass_bot
    #tipo de conteudo (html no caso) 
    msg.add_header('Content-Type', 'text/html')
    #seta o corpo do email
    msg.set_payload(corpo_email )

    try:
        with get_smtp_connection() as s:
            #faz o login normal
            s.login(msg['From'], password)
            #manda o email
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            logger.info('Email enviado com sucesso')
    
    except smtplib.SMTPException as e:
        logger.error(f"Falha ao enviar o email: {e}")