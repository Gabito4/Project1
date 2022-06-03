class Users:

    def __init__(self, user_id=0, username="", password="", email="", isadmin=0):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.isadmin = isadmin

    def __repr__(self):
        return str({
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "isadmin": self.isadmin
        })

    def json(self):
        return {
            "userId": self.user_id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "isadmin": self.isadmin
        }
