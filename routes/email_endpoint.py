from flask import Blueprint, request
from service.email_service import enviar_email
from models.req_model import Req
from models.user_model import User

email_route = Blueprint('email', __name__)

@email_route.route('/mandar_email')
def mandar_email():
    try:
        usuario_mockado = User("gabriel", "pojokjkjk@gmail.com")
        requisicao_mockada = Req(usuario_mockado, "account deletion")
        enviar_email(requisicao_mockada)

    except Exception as e:
        print(e)
    return "email enviado!"