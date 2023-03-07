from abc import ABCMeta, abstractmethod
from typing import Any, List
from pymongo import MongoClient
from models import *


class IRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_persistent_entity(self, key: object) -> (Any | None):
        pass

    @abstractmethod
    def persist_entity(self, object: object) -> bool:
        pass


class UserRepository(IRepository):

    DB_URL = "mongodb://localhost:27017"

    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(__class__.DB_URL)
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
        updateResult = self.collection.update_one(
            {"sequence_nbr": command.sequence_nbr},
            {"$set": {"first_name": command.first_name, "last_name": command.last_name}},
        )
        return updateResult.acknowledged

    def delete_user(self, sequence_nbr: int) -> bool:
        deleteResult = self.collection.delete_one({"sequence_nbr": sequence_nbr})
        return deleteResult.acknowledged

    def delete_all(self) -> bool:
        deleteResult = self.collection.delete_many({})
        return deleteResult.acknowledged

    #### リファクタリング

    def find(self, sequence_nbr: int) -> (User | None):
        return self.__get_persistent_entity(sequence_nbr)

    def persist_entity(self, user: User) -> bool:
        if self.get_persistent_entity(user.sequence_nbr):
            updateResult = self.collection.update_one(
                {"sequence_nbr": user.sequence_nbr},
                {"$set": {"first_name": user.first_name, "last_name": user.last_name}},
            )
            return updateResult.acknowledged
        else:
            insertOneResult = self.collection.insert_one(user.dict())
            return insertOneResult.acknowledged

    def get_persistent_entity(self, sequence_nbr: int) -> (User | None):
        found_user = self.collection.find_one({"sequence_nbr": sequence_nbr})
        return found_user
