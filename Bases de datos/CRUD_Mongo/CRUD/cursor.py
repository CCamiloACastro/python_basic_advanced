from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.animals

# Reset.
db.birds.delete_many({})

# Ingresar pajaros.
db.birds.insert_many([
    {"nombre": "Sparrow", "ubicacion": 10},
    {"nombre": "Bluebird", "ubicacion": 50},
    {"nombre": "Robin", "ubicacion": 10},
    {"nombre": "Colibri", "ubicacion": 10}
])

# Usar buscar e iterar sobre el cursor en for-loop
print("FIND")
cursor = db.birds.find({"ubicacion": 10})
for doc in cursor:
    print(doc)

 # Usar buscar y luego clonar el cursor.
# ... De esta manera podemos evaluarlo dos veces.
print("BUSCAR Y CLONAR")
cursor = db.birds.find({"ubicacion": 50})
cloned_cursor = cursor.clone()
print("CURSOR 1")
for doc in cursor:
    print(doc)
print("CURSOR 2")
for doc in cloned_cursor:
    print(doc)

#Use buscar y luego cuente los resultados.
print("FIND AND COUNT")
cursor = db.birds.count_documents({"ubicacion": 10})
print(cursor)