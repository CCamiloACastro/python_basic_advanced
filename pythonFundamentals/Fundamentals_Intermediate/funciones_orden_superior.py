# Higher Order Functions
from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    """
    Se aprovecha las funciones anteriormente definidas y se ingresan
    como parámetros

    Args:
        first_value: type(int)
        second_value: type(int)
        f_sum: type(function)

    Returns:
        function(first_value + second_value)

    """
    return f_sum(first_value + second_value)


# Closures (una función que encierra otra función)

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value

    return add


add_closure = sum_ten(1)
print(add_closure(5))
# para ingresar los argumentos se concatenan los parenthesis()()...
print((sum_ten(5))(1))

# Built-in Higher Order Functions (funciones de orden superior del propio python

numbers = [2, 5, 10, 21, 3, 30]

"""
map

La función de Map de Python es una función que te permite transformar un iterable completo usando otra función
optimizando código

syntax
map(inserte función aquí, inserte iterable aquí)
"""


def multiply_two(number):
    return number * 2


print(map(multiply_two, numbers))  # <map object at 0x0000021A6DFF6D70>
print(list(map(multiply_two, numbers))) # toca decirle al computador que es una lista
print(list(map(lambda number: number * 2, numbers))) # En vez de una función también se puede usar lambda

"""
filter
Ejecuta una funcion que retorna tru o false para saber como filtrar los valores del iterable
"""


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers))) # sin necesidad de crear una función

"""
reduce
"""


def sum_two_values(first_value, second_value):
    # numbers = [2, 5, 10, 21, 3, 30]
    print(first_value)
    print(second_value)
    # 2+5 = 7 + 10 = 17 + 21 = 38 ... 71
    return first_value + second_value


print(reduce(sum_two_values, numbers))