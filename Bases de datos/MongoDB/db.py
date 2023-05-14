from pymongo import MongoClient
# MongoClient permite la conexion a mongodb

MONGO_URI = 'mongodb://localhost'
# Variable que guarda la ubicacion del servidor, en este caso la PC

client = MongoClient(MONGO_URI)
# Conexion a mongodb, permite trabajar con la base de datos y hacer operaciones con este

db = client['Lista_Pacientes']
collection = db['pacientes']

p1 = {"nombre": "Juan",
      "edad": 35,
      "estrato": 3,
      "correo": "Juan@gmail.com",
      "patologia": "Hipertensión"}
p2 = {"nombre": "María",
      "edad": 28,
      "estrato": 2,
      "correo": "Maria@hotmail.com"}
p3 = {"nombre": "Pedro",
      "edad": 45,
      "estrato": 4,
      "correo": "Pedro@gmail.com",
      "patologia": "Diabetes"
      }
p4 = {"nombre": "Marcos",
      "edad": 19,
      "estrato": 2,
      "correo": "Marcos@gmail.com",
      "patologia": "Trastorno bipolar"}
p5 = {"nombre": "Luna",
      "edad": 22,
      "estrato": 2,
      "correo": "Luna@gmail.com"}
p6 = {"nombre": "Eduardo",
      "edad": 30,
      "estrato": 5,
      "correo": "Eduardo@gmail.com",
      "patologia": "Cáncer de colon"}
p7 = {"nombre": "Oliver",
      "edad": 19,
      "estrato": 2,
      "correo": "Oliver@gmail.com",
      "patologia": "Trastornos de la alimentación"}
p8 = {"nombre": "Charlotte",
      "edad": 45,
      "estrato": 2,
      "correo": "Charlotte@gmail.com",
      "patologia": "Cáncer de mama"}
p9 = {"nombre": "Ethan",
      "edad": 19,
      "estrato": 4,
      "correo": "Ethan@gmail.com"}
p10 = {"nombre": "Isabella",
       "edad": 24,
       "estrato": 3,
       "correo": "Isabella@gmail.com",
       "patologia": "Epilepsia"}
p11 = {"nombre": "Liam",
       "edad": 20,
       "estrato": 1,
       "correo": "Liam@gmail.com",
       "patologia": "Trastornos de ansiedad"}
p12 = {"nombre": "Amelia",
       "edad": 32,
       "estrato": 4,
       "correo": "Amelia@gmail.com",
       "patologia": "Artritis reumatoide"}
p13 = {"nombre": "Noah",
       "edad": 30,
       "estrato": 3,
       "correo": "Noah@gmail.com",
       "patologia": "Esquizofrenia"}
p14 = {"nombre": "Sophia",
       "edad": 18,
       "estrato": 2,
       "correo": "Sophia@gmail.com",
       "patologia": "Cáncer de mama"}
p15 = {"nombre": "Fernando",
       "edad": 19,
       "estrato": 2,
       "correo": "Fernando@gmail.com",
       "patologia": "Cáncer de colon"}
p16 = {"nombre": "Mia",
       "edad": 26,
       "estrato": 2,
       "correo": "Mia@gmail.com"}
p17 = {"nombre": "Benjamin",
       "edad": 29,
       "estrato": 2,
       "correo": "Benjamin@gmail.com",
       "patologia": "Asma"}
p18 = {"nombre": "Harper",
       "edad": 31,
       "estrato": 3,
       "correo": "Harper@gmail.com",
       "patologia": "Trastorno bipolar"}
p19 = {"nombre": "James",
       "edad": 24,
       "estrato": 5,
       "correo": "James@gmail.com",
       "patologia": "Enfermedad de Parkinson"}
p20 = {"nombre": "Evelyn",
       "edad": 25,
       "estrato": 3,
       "correo": "Evelyn@gmail.com"}
p21 = {"nombre": "Lucas",
       "edad": 19,
       "estrato": 2,
       "correo": "Lucas@gmail.com",
       "patologia": "Asma"}
p22 = {"nombre": "Abigail",
       "edad": 19,
       "estrato": 2,
       "correo": "Abigail@gmail.com",
       "patologia": "Depresión"}
p23 = {"nombre": "Alexander",
       "edad": 19,
       "estrato": 2,
       "correo": "Alexander@gmail.com",
       "patologia": "Epilepsia"}

collection.insert_many([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14,
                        p15, p16, p17, p18, p19, p20, p21, p22, p23])

