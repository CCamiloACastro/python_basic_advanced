"""Un objeto es en cierta medida similar a un array, permite agrupar contenido de diferentes tipos de datos
Usualmente, se accede por medio de una array por medio de su índice, en un objeto se accede por medio de una llave key"""

# Creación de un diccionario simple
song = {
    'artista': 'Metallica',
    'cancion': 'Enter Sandman',
    'lanzamiento': 1992,
    'likes': 3300000
}
# Acceder a los elementos del diccionario

print(song['artista'])
print(song['cancion'])

# Agregar nuevos valores (si NO existe lo crea)

song['playlist'] = 'Heavy Metal'
print(song)

# Reemplazar valor existente (si existe lo reemplaza)
song['cancion'] = 'Live to Die'

print(song.items())
print(song.keys())
print(song.values())

# Crear un diccionario de lista o de las claves de otros diccionarios
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(song)
print(my_new_dict)
my_new_dict = dict.fromkeys(song, "vistas")
print(my_new_dict)
# Conversion a otro tipo de datos
print('Conversion a otro tipo de datos')
print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
player = {}
print(player)

# Se une un jugador
player['nombre'] = 'Juan'
player['puntaje'] = 0
print(player)

# Acceder aun valor
print(player.get('nombre'))
print(player.get('edad', 'No existe el valor de edad'))

# Iterar en el diccionario
for keys, values in player.items():
    print(keys)
    print(values)

# Eliminar valores del diccionario
del player['nombre']
print(player)

# Eliminar diccionario

del player
# NameError: name 'player' is not defined
