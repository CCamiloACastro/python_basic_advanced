import os  # libreria para manejar archivos

# Variable toda en MAYÚSCULAS da entender que es una constante
CARPETA = 'contactos/'
EXTENSION = '.txt'


class Contacts:
    def __init__(self, name, phone, category):
        self.name = name
        self.phone = phone
        self.category = category


def create_directory():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)
        print('carpeta creada')


def show_menu():
    print('\nSeleccione del menu lo que desea hacer:\n')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contactos')
    print('5) Eliminar contacto')

    select_option()


def select_option():
    ask = True
    while ask:
        option = input('Seleccione una opción \r\n')
        option = int(option)

        # Ejecutar las opciones
        if option == 1:
            add_contact()
            ask = False
        elif option == 2:
            edit_contacts()
            ask = False
        elif option == 3:
            show_contact()
            ask = False
        elif option == 4:
            search_contact()
            ask = False
        elif option == 5:
            delete_contact()
            ask = False
        else:
            print('Opción no valida')


def exist_contact(name):
    return os.path.isfile(CARPETA + name + EXTENSION)


def add_contact():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto: ')
    numero_contacto = input('Número del contacto: ')
    categoria_contacto = input('Categoría del contacto: ')

    while exist_contact(nombre_contacto):
        print('El nombre de contacto ya existe, favor cambiar de nombre')
        nombre_contacto = input('Nombre del contacto: ')

    if not exist_contact(nombre_contacto):
        # Instanciar la clase
        contacto = Contacts(nombre_contacto, numero_contacto, categoria_contacto)

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            archivo.write('Nombre: ' + contacto.name + '\r\n')
            archivo.write('Teléfono:: ' + contacto.phone + '\r\n')
            archivo.write('Categoría: ' + contacto.category + '\r\n')

        print('\r\n Contacto agregado correctamente \r\n ')


def edit_contacts():
    print('Escribe el nombre del contacto que quieres editar')
    nombre_editar = input('Nombre del contacto que se desea editar \r\n')

    if exist_contact(nombre_editar):
        nombre_contacto = input('Agrega el nuevo Nombre del contacto: ')
        numero_contacto = input('Agrega el nuevo Número del contacto: ')
        categoria_contacto = input('Agrega el nuevo Categoría del contacto: ')

        # Instanciar la clase
        contacto = Contacts(nombre_contacto, numero_contacto, categoria_contacto)

        with open(CARPETA + nombre_editar + EXTENSION, 'w') as archivo:
            archivo.write('Nombre: ' + contacto.name + '\r\n')
            archivo.write('Teléfono:: ' + contacto.phone + '\r\n')
            archivo.write('Categoría: ' + contacto.category + '\r\n')

        os.rename(CARPETA + nombre_editar + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
    else:
        print('El contacto no existe')
        show_menu()


def show_contact():
    archivos = os.listdir(CARPETA)
    print(archivos)
    archivos_txt = [archivo for archivo in archivos if archivo.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')


def search_contact():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as Contacto:
            print('\r\n Información del contacto \r\n')
            for linea in Contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)


def delete_contact():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Archivo eliminado correctamente')
    except IOError:
        print('El archivo no existe')
        print(IOError)


if __name__ == '__main__':
    create_directory()
    show_menu()
