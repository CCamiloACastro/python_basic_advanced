import numpy as np

"""
Search
Puede buscar en una matriz un determinado valor y devolver los índices que obtienen una coincidencia
"""

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)  # the value 4 is present at index 3, 5, and 6
