import user_model

class Req:
    def __init__(self, user:user_model.User, category:str ):
        self.user = user 
        self.category = category 