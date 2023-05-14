# QUERY = consultas

from pymongo import MongoClient
from pymongo import ReturnDocument

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['Lista_Pacientes']
collection = db['pacientes']


"""total_docs = collection.count_documents({})
print(collection.name, " tiene ", total_docs,  " documentos")
"""

# Función find (Busqueda)


# Si se imprime la busqueda dara como resultado un cursor
"""
consulta = collection.find({})
print(consulta)

"""
# Si no se especifica, find({}) muestra todos los documentos de la coleccion
#  Para mostrar todos los resultados  se usa un ciclo for
"""
consulta = collection.find({})
for r in consulta:
    print(r)
"""

# Especificando el criterio de busqueda, se mostrara todos los documentos que cumplan con el criterio
"""
consulta = collection.find({"edad": 19})
for r in consulta:
    print(r)

"""
# find_one muestra el primer documento que coincida con la busqueda
"""
consulta = collection.find_one({"edad": 19})
print(consulta)
"""

# $gt es un operador logico
"""
myquery = {"edad": {"$gt": 29},  "patologia": "Cáncer de mama"}
consulta = collection.find(myquery)
for r in consulta:
    print(r)
"""

# Para realizar cambios dentro de un documento
"""
myquery = collection.find_one_and_update({'nombre':"Fernando"},
                                  { '$set': { "nombre" : 'XXXXXXXXXXXXX'} },
                                  return_document = ReturnDocument.AFTER)
print(myquery)

"""
# Para eliminar un documento
"""
print("Documentos antes del borrado: \n")
consulta = collection.find({"edad": 24})
for r in consulta:
    print(r)

collection.find_one_and_delete({"nombre": "James"})

print("\nDocumentos despues del borrado: \n")
consulta = collection.find({"edad": 24})
for r in consulta:
    print(r)
"""