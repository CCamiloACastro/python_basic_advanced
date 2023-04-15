import numpy as np

# unir y dividir
print('unir')

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

# concatenate 2D arrays
print('concatenate 2D arrays')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)  # Une los primeros array luego los segundos
print(arr)
print('stack function')
arr = np.stack((arr1, arr2), axis=1)
print(arr, arr.ndim)  # Al apilar no se unos los primeros array sino que se apilan (cada array se apila por separado

# stack along rows.
print('stack along rows.')
arr = np.hstack((arr1, arr2))
print(arr)
# stack along columns.
print('stack along columns.')
arr = np.vstack((arr1, arr2))
print(arr)
# stack along height, which is the same as depth.
print('stack along height, which is the same as depth.')
arr = np.dstack((arr1, arr2))
print(arr)

# dividir
print('dividir')
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print('2D arrays split')
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

print('uso de axis en split')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])