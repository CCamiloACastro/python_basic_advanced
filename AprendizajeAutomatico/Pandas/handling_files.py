import pandas as pd

print('\tCSV\n')
df = pd.read_csv('data.csv')

# print(df.to_string())  # tostring prints the entire Dataframe
print(df)  # return only the headers and the first and last 5 rows
# max_rows
print('max_rows')
pd.options.display.max_rows = 50  # si el dataframe es más grande, solo mostrará los primeros 5
print(pd.options.display.max_rows)
print(df)

# Data json
print('\tJson\n')
df = pd.read_json('data.json')

print(df)

# si no se tiene un archivo json sino solamente un diccionario

data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}

df = pd.DataFrame(data)

print(df)

df = pd.read_json('data.json')

print(df.head())  # mira los cinco primeros
print(df.tail())  # mira los cinco últimos
print(df.info())  # information
