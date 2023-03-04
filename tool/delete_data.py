from pymongo import MongoClient
import sys
sys.path.append("../")
from backend.models import *


client: MongoClient = MongoClient('mongodb://localhost:27017')
db = client.users
collection = db.users

deleteResult = collection.delete_many({})
if deleteResult.acknowledged:
    print('おわったよ〜')
else:
    print('ミスったわー')