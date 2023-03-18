"""
Operadores de Pertenencia
Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).

in y not in

"""
languages = ['español', 'ingles', 'aleman', 'japones', 'italiano', 'vietnamita', 'chibcha']

if __name__ == '__main__':
    print(languages)
    # Uso de operadores de pertenencia
    print('ingles' in languages)
    # Ordena alfabeticamente
    languages.sort()
    print(languages)
    # Agregar elemntos a un arreglo
    languages.append('Chino')
    print(languages)
    # Eliminar de un arreglo o list
    del languages[1]
    print(languages)
    # Eliminar el ultimo elemnto
    languages.pop()
    print(languages)
    # Eliminar posicion en especifico
    languages.pop(2)
    print(languages)
    # Eliminar por nombres
    languages.remove('aleman')

    for language in languages:
        print(f'Estoy aprendiendo {language}')

    for num in range(0,10):
        print(num)

    for num in range(0,10,2):
        print(num)
