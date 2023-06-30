from pymongo import MongoClient

# Conectarse a la instancia local de MongoDB
client = MongoClient('mongodb://localhost:27017')

# Acceder a la base de datos y la colección
db = client['nombre_de_la_base_de_datos']
coleccion = db['nombre_de_la_coleccion']

# Crear un documento con un objeto hijo
usuario = {
    "nombre": "Juan",
    "edad": 30,
    "contacto": {
        "email": "juan@example.com",
        "telefono": "123456789",
        "direccion": {
            "calle": "Calle Principal",
            "ciudad": "Ciudad Ejemplo",
            "pais": "País Ejemplo"
        }
    }
}

# Insertar el documento en la colección
#coleccion.insert_one(usuario)

# Consultar documentos con un campo de objeto hijo específico
#resultados = coleccion.find({"contacto.email": "juan@example.com"})
resultados = coleccion.find({"contacto.direccion.ciudad": "Ciudad Ejemplo"})

# Imprimir los resultados
for resultado in resultados:
    print(resultado)