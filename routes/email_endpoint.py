from flask import Blueprint, request
from service.email_service import enviar_email
from models.req_model import Req
from models.user_model import User
from pydantic import ValidationError
import re


def email_valido(email:str):
    regex_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex_email, email) is not None

email_route = Blueprint('email', __name__)

@email_route.route('/mandar_email', methods=['POST'])
def mandar_email():
    try:   

        json_data = request.get_json()
        data = Req(**json_data)

        if not email_valido(data.user.email):
            raise ValidationError('email inválido')
        
        enviar_email(data)

        return {"msg": "Request válido", "data" : data.model_dump()}, 200
    except ValidationError as e:
        print(e)
        return {'error':'corpo da Requisição inválido'}, 400
    except TypeError as e:
        print(e)
        return {'error':'corpo da Requisição inválido'}, 400