# Data types
import numpy as np

"""
strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr)
print(arr.dtype)

# Creating Arrays With a Defined Data Type
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# Converting Data Type on Existing Arrays
print('Converting Data Type on Existing Arrays')
arr = np.array([1.1, 2.1, 3.1, 0])
print(arr.dtype)
new_arr = arr.astype('i')  # arr.astype(int)
print(new_arr)
print(new_arr.dtype)
new_arr = arr.astype(bool)
print(new_arr)
print(new_arr.dtype)

# Copy vs View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is
# just a view of the original array.
# The copy SHOULD NOT be affected by the changes made to the original array
# The view SHOULD be affected by the changes made to the original array
print('copy')
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
print('view')
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# changes in the view
# The original array SHOULD be affected by the changes made to the view.
x = arr.view()
x[0] = 31

print(arr)
print(x)

print('array owns its data')
x = arr.copy()
y = arr.view()

print(x.base)  # The copy returns None.
print(y.base)  # The view returns the original array.
