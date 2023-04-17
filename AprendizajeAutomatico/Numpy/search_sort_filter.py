import numpy as np

"""
Search
Puede buscar en una matriz un determinado valor y devolver los índices que obtienen una coincidencia
"""

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)  # the value 4 is present at index 3, 5, and 6

# numero par
x = np.where(arr % 2 == 0)
print(x)
x = np.where(arr % 2 == 1)
print(x)

# searchsorted()
# devuelve el índice donde se insertaría el valor especificado para mantener el orden de búsqueda
# se asume que la lista esta ordenanada
print('searchsorted()')

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 6)
print(x)

# se devuelve el índice más a la izquierda, con side='right' se retorna el índice más a la derecha en su lugar.

x = np.searchsorted(arr, 7, side='right')
print(x)

# tiene sentido con multiples valores

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

# ordenar
# Este método devuelve una copia de la matriz, dejando la matriz original sin cambios
print('ordenar')
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# filtrar arrays
print('filtrar arrays')

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]  # retorna solo que sea True

print(newarr)

# Create a filter array that will return only values higher than 42
print('Creating Filter using for')

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)


newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Creating Filter Directly From Array
print('Creating Filter Directly From Array')
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42  # debido a que se esta comparando arr con 42 se guarda una lista de Tru y False
print(filter_arr)
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
