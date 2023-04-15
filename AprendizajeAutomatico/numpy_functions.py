"""
Python calls matrices lists, NumPy calls them arrays and TensorFlow calls them tensors
"""
import numpy as np

print(f'Version de numpy: {np.__version__}')
# Array de una dimensión
one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)
print(one_dimensional_array.ndim)

# Para crear una matriz bidimensional, especificar una capa adicional de corchetes
two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)
print(two_dimensional_array.ndim)
# Puede llenar una matriz con una secuencia de números
sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

# Llenar matrices con números aleatorios en ciertos rangos
print('random_integers_between_50_and_100')
random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)

# Para crear valores aleatorios de punto flotante entre 0,0 y 1,0
print('Valores aleatorios tipo float entre 0,0 y 1,0')
random_floats_between_0_and_1 = np.random.random(6)
print(type(random_floats_between_0_and_1))
print(random_floats_between_0_and_1)

# Para sumar o multiplicar hay reglas definidas en algebra básica que hay que seguir,
# sin embargo, cuando se suma ej. una constante se usa un recurso llamado broadcasting
print('sumar 2 al vector')
random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)

print('Multiplicar por 3')
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)

""" 
Ejemplo 1 

Su objetivo es crear un conjunto de datos simple que consta de una sola característica y una etiqueta de la siguiente 
manera: 
Asigne una secuencia de números enteros del 6 al 20 (inclusive) a un array Numpy denominado feature 
Asigne 15 valores a una matriz NumPy denominada label tal que:

"""
print('Ejemplo 1')
feature = np.arange(6, 20)
print(feature)
label = 3 * feature + 4
print(label)

"""
Ejemplo2

Para que su conjunto de datos sea un poco más realista, inserte un poco de ruido aleatorio en cada elemento de la 
matriz de etiquetas que ya creó. 

Para ser más precisos, modifique cada valor asignado a la etiqueta agregando un valor de punto flotante aleatorio 
diferente entre -2 y +2.

NO usar broadcasting

"""
print('Ejemplo 2')
noise = np.random.randint(low=-2, high=2, size=(len(label)))
print(noise)
label = label + noise
print(label)

# Cree una matriz con 5 dimensiones y verifique que tenga 5 dimensiones

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

# indexaciones
# Acceder el elemento de la primera fila, segunda columna

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
print('2nd element on 1st row: [row, columns] ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])

# Acceder el tercer elemento del segundo array del primer array

arr = np.array([
    [[1, 2, 3],
     [4, 5, 6]],
    [[7, 8, 9],
     [10, 11, 12]]
])
print(arr)
print(arr[0, 1, 2])

# negative indexing

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
print('Last element from 2nd dim: ', arr[1, -1])

# Array Slicing
print('Array Slicing')
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # Note: The result includes the start index, but excludes the end index.
print(arr[4:])  # index 4 to the end of the array
print(arr[:4])  # Slice elements from the beginning to index 4 (not included)
print(arr[-3:-1])  # excludes the end index
print(arr[1:6:2])  # Por pasos
print(arr[::2])  # Devuelve todos los demás elementos de toda la matriz

# Slicing 2D arrays
print('Slicing 2D arrays')
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])  # from the second array, from 1 to 4 (not included)
print(arr[0:2, 2])  # De ambos arrays devuelve el index 2
print(arr[0:2, 1:4])  # De ambos arrays devuelve del elemento en la posición 1 hasta la tres
