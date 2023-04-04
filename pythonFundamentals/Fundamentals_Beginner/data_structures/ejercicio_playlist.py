playlist = {'titulo': [], 'canciones': []}
print(playlist)


def app():
    """
    Aplicación principal donde se coloca un título a una playlist
    y se agregan playlist
    Returns:

    """
    add_playlist = True

    while add_playlist:
        name_playlist = input('¿Como desea nombrar la playlist?: \r\n')
        # si el nombre no esta vacio
        if name_playlist.lower() == 'x':
            print('finalizando...')
            add_playlist = False
        elif name_playlist:
            playlist['titulo'].append(name_playlist)
            add_songs()
            print(playlist)
        else:
            print(playlist)
            print('El campo Titulo no puede quedar vacio')



        # Agregar canciones



def add_songs():
    """
    [Description]
    Añadir canciones
    Returns:
        no retonra nada

    """
    print('Agregar canciones')
    add_song = True
    while add_song:
        name_playlist = playlist['titulo']
        pregunta = f'Agregar canciones para la playlist: {name_playlist} \r\n'
        pregunta += '(Escribe x para dejar de agregar canciones)\r\n'

        song = input(pregunta)
        if song.lower() == 'x':
            break
        else:
            # Agregar canciones
            playlist['canciones'].append(song)
            show_songs(name_playlist)


def show_songs(name_playlist):
    """
    [Description]
    Funcion que se usara para mostrar la lista de canciones
    de una manera organizada

    Args:
        name_playlist: nombre de la playlist a la cual se le va a
        mostrar el nombre de las canciones

    Returns:
        No retorna nada

    """

    print(f'Playlist {name_playlist}')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(f'{cancion}\r\n')


app()
