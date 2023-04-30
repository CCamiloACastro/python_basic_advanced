import pymongo
import json


# establecer conexión con la base de datos
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CRUD"]
coleccion = db["Clase"]

# cargar los documentos en un archivo JSON
with open('datos.json') as file:
    json_data = json.load(file)


coleccion.insert_one(json_data)
