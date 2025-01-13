from services.email_service import enviar_email
from models.req_model import Req
from models.user_model import User

usuario_mockado = User("aaaa", "aaa@gmail.com")
requisicao_mockada = Req(usuario_mockado, "account deletion")

enviar_email(requisicao_mockada)