from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["CRUD"]
coleccion = db["Clase"]

# Insertar varios documentos
documentos = [
    {"nombre": "David", "edad": 20},
    {"nombre": "María", "edad": 30},
    {"nombre": "Pedro", "edad": 40}
]
resultado = coleccion.insert_many(documentos)
print(resultado.inserted_ids)
