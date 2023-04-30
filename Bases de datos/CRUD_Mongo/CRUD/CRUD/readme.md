pip install pymongo

CRUD,
Crear y borrar,
Insert.json,
insert(),
insertone(),
insert Many(),
remove(),
insert para un array de objetos,
tipos bson.

CRUD, Crear y borrar, Insert.json, remove(), tipos bson.

Crear un documento

    En MongoDB, existen tres métodos principales para insertar documentos en una colección: insert(), insert_one() e insert_many().

    La principal diferencia entre ellos radica en la cantidad de documentos que se pueden insertar de una sola vez:

    insert() permite la inserción de uno o varios documentos en una colección.
    insert_one() permite la inserción de un solo documento en una colección.
    insert_many() permite la inserción de varios documentos en una colección.
    Además, también hay diferencias en la forma en que manejan las excepciones y la forma en que devuelven el resultado de la operación de inserción.

    insert() devuelve un objeto InsertOneResult, que contiene información sobre la operación de inserción, incluyendo el número de documentos insertados y los identificadores generados automáticamente para los documentos insertados.

    insert_one() devuelve un objeto InsertOneResult similar a insert(), pero solo para un solo documento.

    insert_many() devuelve un objeto InsertManyResult, que contiene información sobre la operación de inserción, incluyendo el número de documentos insertados y los identificadores generados automáticamente para los documentos insertados.

    Es importante destacar que, en general, es más eficiente insertar varios documentos a la vez utilizando insert_many() en lugar de insertarlos uno por uno con insert_one() o insert(). Esto se debe a que insert_many() reduce la cantidad de operaciones de red necesarias para insertar varios documentos, lo que puede mejorar significativamente el rendimiento en entornos de alta carga.

    El método insert() ya no existe en las últimas versiones de PyMongo (a partir de la versión 4.0). En su lugar, se recomienda utilizar los métodos insert_one o insert_many dependiendo de si quieres insertar un solo documento o varios documentos, respectivamente.

Leer un Documento

    La principal diferencia entre find() y find_one() es que find() devuelve un cursor que contiene todos los documentos que coinciden con los criterios de búsqueda, mientras que find_one() devuelve solamente el primer documento que cumple con los criterios de búsqueda especificados.

Actualizar un documento

    En MongoDB, update(), update_one() y update_many() son métodos que se utilizan para actualizar documentos en una colección que cumplan con los criterios de búsqueda especificados.

    La principal diferencia entre estos métodos es la cantidad de documentos que se actualizan:

    update() actualiza todos los documentos que coinciden con los criterios de búsqueda especificados.
    update_one() actualiza solamente el primer documento que cumple con los criterios de búsqueda especificados.
    update_many() actualiza todos los documentos que coinciden con los criterios de búsqueda especificados.

    El método update() ya no está disponible en la versión más reciente de pymongo. En su lugar, se debe utilizar el método update_one() o update_many() dependiendo del caso.

Eliminar un Documento

    La diferencia entre delete_one() y delete_many() en MongoDB es que delete_one() borra solamente el primer documento que cumple con los criterios de búsqueda especificados, mientras que delete_many() borra todos los documentos que cumplan con dichos criterios.

    Si en la colección hay varios documentos que cumplen con los criterios de búsqueda especificados, delete_one() solo borrará el primer documento que encuentre y no afectará a los demás documentos. En cambio, delete_many() borrará todos los documentos que cumplan con los criterios de búsqueda.
