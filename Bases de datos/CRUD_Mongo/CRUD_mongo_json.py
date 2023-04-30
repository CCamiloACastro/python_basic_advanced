from pymongo import MongoClient

client = MongoClient('localhost', 27017)
print(client)

db = client.test
col = db.person

print(db)
print(col)
