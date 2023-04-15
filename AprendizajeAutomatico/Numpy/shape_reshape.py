import numpy as np
# shape
print('shape')

print(arr.shape)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# Reshaping arrays
print('Reshaping arrays')
print('Reshape From 1-D to 2-D')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 4)
print(newarr)
print('Reshape From 1-D to 3-D')
newarr = arr.reshape(2, 3, 2)  # 2 matrices que contienen 3 matrices, cada una con 2 elementos
# Como ayuda tomar desde la dimensión más externa
print(newarr)

# Unknown Dimension
print('Unknown Dimension')
# significa que no se tiene que especificar el número exacto para una de las dimensiones del método reshape
# Note: We can not pass -1 to more than one dimension.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)  # 2 matrices con 2 matrices internas, los elementos desconocidos [-1]
print(newarr)

# Flattening the arrays (Aplanar) convert multidimensional arrya into a 1D array
print('Flattening the arrays')
newarr = arr.reshape(-1)
print(newarr)
