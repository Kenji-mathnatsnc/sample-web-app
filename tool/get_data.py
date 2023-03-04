from pymongo import MongoClient

client: MongoClient = MongoClient('mongodb://localhost:27017')
db = client.users
collection = db.users

found_users = []
cursor = collection.find()
for document in cursor:
    found_users.append(document)

print(found_users)
