from flask import Blueprint, request
from services.email_service import enviar_email
from models.req_model import Req
from models.user_model import User

email_route = Blueprint('email', __name__)

@email_route.route('/mandar_email')
def mandar_email():
    try:
        enviar_email()
    except Exception as e:
        print(e)
    return "email enviado!"