"""
Python calls matrices lists, NumPy calls them arrays and TensorFlow calls them tensors
"""
import numpy as np

# Array de una dimensión
one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)

# Para crear una matriz bidimensional, especificar una capa adicional de corchetes
two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)

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
