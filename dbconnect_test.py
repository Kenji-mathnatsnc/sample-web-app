
import mysql.connector
from pymongo import MongoClient

cnx = None

try:
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        # password='password',  # パスワード
        host='localhost'  # ホスト名(IPアドレス）
    )

    if cnx.is_connected:
        print("Connected to MySQL !!")
        cursor = cnx.cursor()
        sql = ('select * from auth.test')
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()


client: MongoClient = MongoClient('mongodb://127.0.0.1:27017')
db = client.users
collection = db.users
found_users = []
cursor = collection.find()
print('Connected to MongoDB !!')
for document in cursor:
    print(document)
