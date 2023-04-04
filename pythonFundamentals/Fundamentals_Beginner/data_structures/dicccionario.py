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
