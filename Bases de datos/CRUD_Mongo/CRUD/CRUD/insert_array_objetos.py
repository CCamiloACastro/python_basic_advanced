from pymongo import MongoClient

# Establecer la conexión con MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["CRUD"]
coleccion = db["Clase"]

# Crear un documento con un array de objetos
documento = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "hobbies": [
        {"nombre": "Fútbol", "nivel": "Alto"},
        {"nombre": "Pintura", "nivel": "Medio"},
        {"nombre": "Cocina", "nivel": "Bajo"}
    ]
}

# Insertar el documento en la colección
coleccion.insert_one(documento)
