from typing import Dict, List

class UserService:
    users: List[Dict[str, str]] = []

    def __init__(self):
        self.users = []

    def create_user(self, name: str, email: str) -> Dict[str, str]:
        user = {'name': name, 'email': email}
        self.users.append(user)
        return user

    def get_users(self) -> List[Dict[str, str]]:
        return self.users
