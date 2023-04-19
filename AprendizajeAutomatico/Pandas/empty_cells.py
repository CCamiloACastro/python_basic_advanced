"""
Se puede corregir

eliminando celdas
reemplazando los valores nulos por un valor arbitrario o usando la media, la moda o la mediana
"""

import pandas as pd

pd.options.display.max_rows = 15


def information(dataframe):
    # print(dataframe.to_string())
    print(dataframe)
    print(dataframe.info())  # information


def remove_rows(dataframe):
    # By default, the dropna() method returns a new DataFrame, and will not change the original
    # df.dropna(inplace = True) modificara el original
    print('Remove Rows')
    new_df = dataframe.dropna()
    information(new_df)


def replace_any_values(dataframe):
    print('replace values in any column')
    new_df = dataframe.fillna(130)
    information(new_df)


def replace_column_value(dataframe, column: str, value):
    dataframe[column].fillna(value, inplace=True)  # modifica el original
    information(dataframe)


df = pd.read_csv('data2.csv')
information(df.copy())
remove_rows(df.copy())
replace_any_values(df.copy())
print('Reemplazar columna con cualquier valor')
replace_column_value(df.copy(), column='Calories', value=1000)
# Media o Promedio
x = df["Calories"].mean()
print(f'Reemplazar con la media {x}')
replace_column_value(df.copy(), column='Calories', value=x)
# Moda
x = df["Calories"].mode()[0]
print(f'Reemplazar con la moda {x}')
replace_column_value(df.copy(), column='Calories', value=x)
# Mediana
x = df["Calories"].median()
print(f'Reemplazar con la mediana: {x}')
replace_column_value(df.copy(), column='Calories', value=x)
