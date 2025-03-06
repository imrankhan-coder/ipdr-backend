class AuthContext:
    def __init__(self):
        self.authenticated_users = {}

    def authenticate(self, user_id):
        self.authenticated_users[user_id] = True

    def is_authenticated(self, user_id):
        return self.authenticated_users.get(user_id, False)
