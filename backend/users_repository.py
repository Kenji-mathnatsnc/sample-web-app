from typing import List
from pymongo import MongoClient
from models import *


class UserRepository():

    DB_URL = 'mongodb://localhost:27017'

    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(self.DB_URL)
        self.db = self.client.users
        self.collection = self.db.users

    def get_all_users(self) -> list:
        found_users = []
        cursor = self.collection.find()
        for document in cursor:
            found_users.append(User(**document))
        return found_users

    def get_user(self, sequence_nbr: int) -> (User | None):
        found_user = self.collection.find_one({"sequence_nbr": sequence_nbr})
        if found_user:
            return User(**found_user)

    def create_user(self, user: User) -> bool:
        insertOneResult = self.collection.insert_one(user.dict())
        return insertOneResult.acknowledged

    def create_many_users(self, user_list: List[User]) -> bool:
        insertManyResult = self.collection.insert_many(user_list)
        return insertManyResult.acknowledged

    def update_user(self, command: UpdateUserCommand) -> bool:
        updateResult = self.collection.update_one({"sequence_nbr": command.sequence_nbr},
                                                  {"$set": {"first_name": command.first_name,
                                                            "last_name": command.last_name}})
        return updateResult.acknowledged

    def delete_user(self, sequence_nbr: int) -> bool:
        deleteResult = self.collection.delete_one(
            {"sequence_nbr": sequence_nbr})
        return deleteResult.acknowledged

    def delete_all(self) -> bool:
        deleteResult = self.collection.delete_many({})
        return deleteResult.acknowledged
