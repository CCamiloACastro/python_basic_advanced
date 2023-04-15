import numpy as np

# Iterating Arrays
print('Iterating Arrays')

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('Firsts iterate')
for x in arr:
    print(x)
print('Second iterate')
for x in arr:
    for y in x:
        for z in y:
            print(z)

# can be difficult to write for arrays with very high dimensionality.
print('nditer()')
for x in np.nditer(arr):
    print(x)

# Cambiar el tipo de datos durante la iteracion
"""
NumPy no cambia el tipo de datos del elemento en el lugar (donde el elemento está en la matriz), 
por lo que necesita otro espacio para realizar esta acción, ese espacio adicional se llama búfer, 
y para habilitarlo en nditer() nosotros pasar flags=['buffered'].
"""
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# Iterating With Different Step Size
print('Iterating With Different Step Size')
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):  # Tome todos los array (array 1 y 2) luego coja todos y sáltese de a 2
    print(x)

# Enumerar
print('Enumerar')

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)

