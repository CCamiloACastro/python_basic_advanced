def app():
    archivo = open('archivo.txt', 'w')  # w es de escritura por default es lectura

    # Generar numeros en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea' + str(i) + '\r\n')

    # Cerrar el archivo
    archivo.close()


def app2():
    # with open es una función más nueva, el archivo se cierra automáticamente
    # as es como crear un alias
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())
            

app()
app2()
