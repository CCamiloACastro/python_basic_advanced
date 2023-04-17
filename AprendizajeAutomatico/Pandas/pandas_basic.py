import pandas as pd

print(pd.__version__)

my_dataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
my_var = pd.DataFrame(my_dataset)
print(my_var)

# una serie es como una columna en una tabla, una array 1D que contiene datos de cualquier tipo

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])  # index con label
print(myvar[1])
print(myvar[2])

# create labels
print('create labels')
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])

# dictionary in pandas
print('dict in pandas')
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)  # Note: The keys of the dictionary become the labels.
print('choose just someones')
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)

"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
    Series is like a column, a DataFrame is the whole table.
"""
print('\nndataframes\n')
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
print('loc -> localizar filas rows')
print(df.loc[0])
# use a list of indexes:
print(df.loc[[0, 1]])
# Named Indexes
print('Named Indexes')
df = pd.DataFrame(data, index=["day1", "day2", "day3"]) # los index deben ser string
print(df)
