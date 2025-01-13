from models.user_model import User

class Req:
    def __init__(self, user:User, category:str ):
        self.user = user 
        self.category = category 