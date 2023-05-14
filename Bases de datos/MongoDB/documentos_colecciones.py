from pymongo import MongoClient
# MongoClient permite la conexion a mongodb

MONGO_URI = 'mongodb://localhost'
# Variable que guarda la ubicacion del servidor, en este caso la PC

client = MongoClient(MONGO_URI)
# Conexion a mongodb, permite trabajar con la base de datos y hacer operaciones con este

db = client['Tienda_de_prueba']
# Creacion de una base de datos
collection = db['productos']
# Creacion de una nueva coleccion

collection.insert_one({"_id": 1,
                       "nombre": "teclado",
                       "precio": 300})
# Creacion de un documento (dato)
# _id permite dar un numero de id al documento que se crea, si no se indica mongo se lo asigna automaticamente

producto_1 = {"_id": 2,
              "nombre": "mouse"}
producto_2 = {"_id": 3,
               "nombre": "monitor"}
producto_3 = {"_id": 4,
              "nombre": "laptop",
              "color": "negro",
              "activo": True,
              "precio": 402}
producto_4 = {"raza": "Pastor Aleman",
              "color": "negro"}

# Creacion de documentos para insertar al mismo tiempo en una sola operacion

collection.insert_many([producto_1, producto_2, producto_3, producto_4])
# Para insertar varios documentos en la misma coleccion a la vez, se insertan en una lista y se usa la instruccion
# insert_many
