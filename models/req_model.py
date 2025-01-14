from models.user_model import User
from pydantic import BaseModel

class Req(BaseModel):
        user:User 
        category:str 