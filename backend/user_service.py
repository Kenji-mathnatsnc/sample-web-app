from models import *
from users_repository import *


class UserService:
    user_repo: UserRepository

    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    def find(self, sequence_nbr: int) -> (User | None):
        result = self.user_repo.get_user(sequence_nbr)
        return result

    def find_all(self) -> list:
        return self.user_repo.get_all_users()

    def register(self, sequence_nbr: int, first_name: str, last_name: str, gender: str, roles: str) -> bool:
        user = User(sequence_nbr=sequence_nbr, first_name=first_name, last_name=last_name, gender=gender, roles=roles)
        result = self.user_repo.create_user(user)
        return result

    def update(self, sequence_nbr: int, first_name: str, last_name: str) -> bool:
        command = UpdateUserCommand(sequence_nbr=sequence_nbr, first_name=first_name, last_name=last_name)
        result = self.user_repo.update_user(command)
        return result

    def remove(self, sequence_nbr: int) -> bool:
        result = self.user_repo.delete_user(sequence_nbr)
        return result

    def remove_all(self) -> bool:
        result = self.user_repo.delete_all()
        return result
