from pymongo import MongoClient

try:
    # establecer conexión con MongoDB
    client = MongoClient("mongodb://localhost:27017")
    db = client["CRUD"]
    coleccion = db["Clase"]

    '''
                        Funcion delete_one()
    borrar un documento que cumpla los criterios especificados
    '''
    # result = coleccion.delete_one({"nombre": "Pedro"})

    '''
                        Funcion delete_many()
    borrar varios documentos que cumplan los criterios especificados
    '''
    result = coleccion.delete_many({"edad": 55})
    
    # imprimir el número de documentos borrados
    print("Se elimino " + str(result.deleted_count) + " registro(s)")

except Exception as e:
    print(e)