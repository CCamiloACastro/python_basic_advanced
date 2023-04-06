# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario <class 'dict'>

my_other_set = {"Camilo", "Castro", 24}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("Colombia")

print(my_other_set)  # Un set no es una estructura ordenada por lo que
# print(my_other_set[1]) # no hay control sobre la posición

my_other_set.add("Colombia")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Camilo" in my_other_set)
print("camilo" in my_other_set)

# Eliminación

my_other_set.remove("Castro")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Matlab", "C++", 10}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

# Union de dos listas
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union(
    {"JavaScript", "C#"}))  # ignora los union porque ya están en el set
print(my_new_set.difference(my_set))  # No aparece "JavaScript", "C#" porque se hizo dentro del print
