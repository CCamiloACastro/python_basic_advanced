from pymongo import MongoClient
#Select the database to use.
use('Usuarios');

#Insert a few documents into the sales collection.
db.getCollection('Personas').insertMany([
  { 'Nombre': 'Andres',   'Edad': 18, 'hobbies': ["Fútbol", "Cine"]},
  { 'Nombre': 'Juan',     'Edad': 20, 'hobbies': ["Leer", "Correr"]},
  { 'Nombre': 'Rocio',    'Edad': 23, 'hobbies': ["Musica", "Cine"]},
  { 'Nombre': 'Carolina', 'Edad': 25, 'hobbies': ["Viajar", "Leer"]},
  { 'Nombre': 'Javier',   'Edad': 15, 'hobbies': ["Correr", "Musica"]},
])
db.Personas.updateOne(
    {_id: '1'},
    {
    $set: {hobbies:["Leer", ""],fecha_actualizacion: true}
    }
)ObjectId("646551c59f3ec6cad8767b3b")
#Actualizar valor y fecha
db.Personas.updateOne({Edad: 18}, {$set: {Nombre: 'Sofia'}, $currentDate:{Fecha_Actualizacaion: true}});
#Actualizar documento
db.Personas.updateOne({"Edad":18},{'$inc':{"cantidad":0}})