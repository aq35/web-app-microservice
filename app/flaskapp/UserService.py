# UserService.py

class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, name: str, email: str) -> dict:
        user = {'name': name, 'email': email}
        self.users.append(user)
        return user

    def get_users(self) -> list[dict]:
        return self.users
