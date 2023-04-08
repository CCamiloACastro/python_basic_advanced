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


my_list = [sum_five(i) for i in range(8)]
print(my_list)

# Sin lista de comprensión

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# con lista de comprensión

newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
# devuelve el item si no es banana, si es banana devuelve orange"
# debido a que la condición no devuelve True, NO es un filtro sino un manipulador del resultado
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
