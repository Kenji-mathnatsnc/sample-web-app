from pymongo import MongoClient
import sys
sys.path.append("../")
from backend.models import *


client: MongoClient = MongoClient('mongodb://localhost:27017')
db = client.users
collection = db.users

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
    ).dict()
]
insertManyResult = collection.insert_many(user_data)
if insertManyResult.acknowledged:
    print('おわったよ〜')
else:
    print('ミスったわ〜')