"""
Operadores de Pertenencia
Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).

"in" y "not in"

"""
languages = list()
my_new_languages = []
print(type(languages))
languages = ['español', 'ingles', 'aleman', 'japones', 'italiano', 'vietnamita', 'chibcha']

if __name__ == '__main__':
    print(languages)
    # Uso de operadores de pertenencia
    print('ingles' in languages)
    # Ordena alfabéticamente
    languages.sort()
    print(languages)
    # Agregar elementos a un arreglo
    languages.append('Chino')
    print(languages)
    # Agregar elemento en una posición concreta
    languages.insert(4, 'Catalan')
    print(languages)
    # Eliminar de un arreglo o list (elimina por índice)
    del languages[1]
    print(languages)
    # Eliminar el último elemento
    languages.pop()
    print(languages)
    # Eliminar posición en específico
    var_pop = languages.pop(2)
    print(var_pop)
    print(languages)
    # Eliminar por nombres
    languages.remove('aleman')
    print(languages)
    # Operaciones con listas

    my_new_languages = languages.copy()

    languages.clear()
    print(languages)
    print(my_new_languages)

    my_new_languages.reverse()
    print(my_new_languages)

    my_new_languages.sort()
    print(my_new_languages)

    # Sublistas

    print(my_new_languages[1:3])

    # Indices
    print(my_new_languages[0])
    print(my_new_languages[-1])
    print(my_new_languages[-2])
    print(my_new_languages[-3])
    print(my_new_languages[-4])

    # Recorrer una lista
    for language in my_new_languages:
        print(f'Estoy aprendiendo {language}')
    # Creación de una lista a partir de un rangoo
    numbers = list(range(0, 10))
    print(numbers)
    for num in numbers:
        print(num)
    # Recorrer una lista de 2 en 2
    for num in range(0, 10, 2):
        print(num)

    # Concatenar
    print(my_new_languages + numbers)
