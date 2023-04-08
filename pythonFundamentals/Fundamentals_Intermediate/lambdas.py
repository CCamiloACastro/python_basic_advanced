"""
Una función lambda es una pequeña función anónima.
Una función lambda puede tomar cualquier cantidad de argumentos, pero solo puede tener una expresión.
Una lambda se puede almacenar en una variable

Syntax
lambda arguments: expression
"""

# Utilice funciones lambda cuando se requiera una función anónima durante un breve período de tiempo.
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(7, 3))

multiply_two_values = lambda first_value, second_value: first_value * second_value
print(multiply_two_values(7, 3))


# una lambda puede estar en una función

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(4)(3, 2))
