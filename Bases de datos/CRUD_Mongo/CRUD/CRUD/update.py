from pymongo import MongoClient

try: 
    # establecer conexión con MongoDB
    client = MongoClient("mongodb://localhost:27017")
    db = client["CRUD"]
    coleccion = db["Clase"]

    '''
                        Funcion update()
    actualizar todos los documentos que cumplan los criterios especificados
    '''
    # coleccion.update({"nombre": "Juan"}, {"$set": {"edad": 55}})

    '''
                        Funcion update_one()
    actualizar el primer documento que cumpla los criterios especificados
    '''
    # coleccion.update_one({"nombre": "Juan"}, {"$set": {"edad": 25}})

    '''
                        Funcion update_many()
    actualizar todos los documentos que cumplan los criterios especificados
    '''
    coleccion.update_many({"nombre": "Juan"}, {"$set": {"edad": 55}})

except Exception as e:
    print("Error en la actualización: ", e)
