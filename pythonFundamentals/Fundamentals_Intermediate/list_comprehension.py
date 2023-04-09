# List Comprehension
"""
La expresión es el elemento actual en la iteración, pero también es el resultado, que puede manipular antes de
que termine como un elemento de lista en la nueva lista

Syntax ->  newlist = [expression for item in iterable if condition == True]

Expression
La expresión es el elemento actual en la iteración, pero también es el resultado, que puede manipular antes de que
termine como un elemento de lista en la nueva lista
Condition
La condition es como un filtro que solo acepta los items que se valoran como verdadero.
La expresión también puede contener condiciones, no como un filtro, sino como una forma de manipular el resultado

Iterable
La parte iterable puede ser cualquier objeto iterable, como una list, tuple, set etc.
Un range tampien se puede uasr como funcion iterable

"""
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

# Definición

my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)


def sum_five(number):
    return number + 5


print("Sumar cinco a un alista de 0-7")
my_list = [sum_five(i) for i in range(8)]
print(my_list)
my_list = [i + 5 for i in range(8)]
print(my_list)
# la función map se explica en el script funciones_orden_superior
my_list = list(map(lambda i: i + 5, range(8)))
print(my_list)

# Sin lista de comprensión

print('Sin lista de comprensión')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for fruit in fruits:
    if "a" in fruit:
        newlist.append(fruit)

print(newlist)

# con lista de comprensión

print('con lista de comprensión')

newlist = [fruit for fruit in fruits if "a" in fruit]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
# devuelve el item si no es banana, si es banana devuelve orange"
# debido a que la condición no devuelve True, NO es un filtro sino un manipulador del resultado
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
