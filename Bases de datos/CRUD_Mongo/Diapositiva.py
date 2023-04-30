from pymongo import MongoClient
client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb
db = client.test
col = db.person

db.SalesDB.insert_one({
    "name": "Linda",
    "orderdate": "6/10/2021",
    "species": "Dog",
    "ownerAddress": "380 W. Fir Ave",
    "chipped": True
})

