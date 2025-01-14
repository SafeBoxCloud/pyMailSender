from flask import Blueprint, request
from service.email_service import enviar_email
from models.req_model import Req
from models.user_model import User
from pydantic import ValidationError
from validate_email import validate_email 

email_route = Blueprint('email', __name__)

@email_route.route('/mandar_email', methods=['POST'])
def mandar_email():
    try:   

        json_data = request.get_json()
        data = Req(**json_data)
        is_valid = validate_email(data.user.email)

        if not is_valid:
            raise ValidationError('email inválido')
        
        enviar_email(data)

        return {"msg": "Request válido", "data" : data.model_dump()}, 200
    except ValidationError as e:
        print(e)
        return {'error':'corpo da Requisição inválido'}, 400
    except TypeError as e:
        print(e)
        return {'error':'corpo da Requisição inválido'}, 400