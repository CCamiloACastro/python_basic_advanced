from pymongo import MongoClient

#Listado de operadores relacionales
''' 
        $eq - equal - igual
        $lt - low than - menor que
        $lte - low than equal - menor o igual que
        $gt - greater than - mayor que
        $gte - greater than equal - mayor o igual que
        $ne - not equal - distinto
        $in - in - dentro de
        $nin - not in - no dentro de
    '''

try:
    # establecer conexión con MongoDB
    client = MongoClient("mongodb://localhost:27017")

    db = client["CRUD"]
    coleccion = db["Clase"]


    # Funcion find()
    '''
    # buscar todos los documentos que cumplan los criterios especificados
    cursor = list(coleccion.find({"edad": {"$lt": 55}}))
    
    # obtener el número de documentos encontrados
    num_documentos = len(cursor)

    # si no se encontraron documentos, imprimir mensaje
    if num_documentos == 0:
        print("No hay registros")
    else:
        # recorrer el cursor e imprimir los documentos
        for document in cursor:
            print(document)
    '''
    

    # Funcion find_one()
    '''
    # leer un documento que cumpla los criterios especificados
    document = coleccion.find_one({"nombre": "Juan"})
    # Verificar si existen registros
    if document is None:
        print("No hay registros")
    else:
        # imprimir el documento encontrado
        print(document)
    '''
    

except Exception as e:
    print(e)