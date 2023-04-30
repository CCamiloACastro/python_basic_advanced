from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["CRUD"]
coleccion = db["Clase"]

# Insertar un documento
documento = {"nombre": "Juan", "edad": 25}
resultado = coleccion.insert(documento)
print(resultado)