from models import *
from users_repository import UserRepository


class UserService():
    user_repo: UserRepository

    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    def find(self, sequence_nbr: int):
        result = self.user_repo.get_user(sequence_nbr)
        return result

    def find_all(self):
        return self.user_repo.get_all_users()

    def register(self, user: User):
        result = self.user_repo.create_user(user)
        return result

    def update(self, command: UpdateUserCommand):
        result = self.user_repo.update_user(
            command.sequence_nbr, command.first_name, command.last_name)
        return result

    def remove(self, sequence_nbr: int):
        result = self.user_repo.delete_user(sequence_nbr)
        return result

    def remove_all(self):
        result = self.user_repo.delete_all()
        return result
