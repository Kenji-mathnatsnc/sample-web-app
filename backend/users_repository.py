from typing import List
from pymongo import MongoClient
from models import *

# DB_URL = 'mongodb+srv://test:test@cluster0.zvseqwf.mongodb.net/?retryWrites=true&w=majority'
DB_URL = 'mongodb://127.0.0.1:27017'


class UserRepository():

    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(DB_URL)
        self.db = self.client.users
        self.collection = self.db.users
        if len(self.get_all_users()) == 0:
            self.init_db()

    def init_db(self):
        user_data: List[User] = [
            User(
                sequence_nbr=1,
                first_name="坂上",
                last_name="田村麻呂",
                gender=Gender.male,
                roles=Role.user,
            ).dict(),
            User(
                sequence_nbr=2,
                first_name="空条",
                last_name="徐倫",
                gender=Gender.female,
                roles=Role.user,
            ).dict(),
            User(
                sequence_nbr=3,
                first_name="ハリウッド",
                last_name="ザコシショウ",
                gender=Gender.male,
                roles=Role.user,
            ).dict(),
            User(
                sequence_nbr=4,
                first_name="世紀末覇者",
                last_name="ラオウ",
                gender=Gender.male,
                roles=Role.admin,
            ).dict(),
        ]
        print('初期データinsert')
        self.create_many_users(user_data)

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
