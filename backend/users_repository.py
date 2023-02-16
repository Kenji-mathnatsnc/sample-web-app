from typing import List
from pymongo import MongoClient
from models import Gender, User, Role


class UserRepository():

    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(
            'mongodb+srv://test:test@cluster0.zvseqwf.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client.users
        self.collection = self.db.users
        if len(self.get_all_users()) == 0:
            self.init_db()

    def init_db(self):
        user_data: List[User] = [
            User(
                sequence_nbr=1,
                first_name="aaaaa",
                last_name="bbbbb",
                gender=Gender.male,
                roles=[Role.user],
            ).dict(),
            User(
                sequence_nbr=2,
                first_name="ccccc",
                last_name="ddddd",
                gender=Gender.female,
                roles=[Role.user],
            ).dict(),
            User(
                sequence_nbr=3,
                first_name="HollyWood",
                last_name="Zakoshisho",
                gender=Gender.male,
                roles=[Role.user],
            ).dict(),
            User(
                sequence_nbr=4,
                first_name="世紀末覇者",
                last_name="ラオウ",
                gender=Gender.male,
                roles=[Role.admin, Role.user],
            ).dict(),
        ]
        print('初期データinsert')
        self.create_many_users(user_data)

    def get_all_users(self):
        found_users = []
        cursor = self.collection.find()
        for document in cursor:
            found_users.append(User(**document))
        return found_users

    def get_user(self, sequence_nbr: int):
        found_user = self.collection.find_one({"sequence_nbr": sequence_nbr})
        if found_user:
            return User(**found_user)

    def create_user(self, user: User):
        insertOneResult = self.collection.insert_one(user.dict())
        return insertOneResult.acknowledged

    def create_many_users(self, user_list: List[User]):
        insertManyResult = self.collection.insert_many(user_list)
        return insertManyResult.acknowledged

    def update_user(self, sequence_nbr: int, first_name: str, last_name: str):
        updateResult = self.collection.update_one({"sequence_nbr": sequence_nbr},
                                                  {"$set": {"first_name": first_name, "last_name": last_name}})
        return updateResult.acknowledged

    def delete_user(self, sequence_nbr: int):
        deleteResult = self.collection.delete_one(
            {"sequence_nbr": sequence_nbr})
        return deleteResult.acknowledged

    def delete_all(self):
        deleteResult = self.collection.delete_many({})
        return deleteResult.acknowledged
