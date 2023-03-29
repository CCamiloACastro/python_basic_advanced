import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine  # (pip install --upgrade 'sqlalchemy<2.0’)

# Crear un DataFrame de ejemplo
data = {'columna1': [1, 2, 3, 4, 5],
        'columna2': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)
# create_engine('tipo_de_base_de_datos://usuario:contraseña@host:puerto/base_de_datos')
conn = create_engine('mysql+pymysql://root:1234567890@localhost:3306/ejercicio4')
df.to_sql('columnas', conn)
print('Dataframe original')

# Ejecutar un query (1)
df = pd.read_sql("SELECT * FROM columnas", conn)
print('Dataframe desde SQL')
print(df)
# Crear un histograma de la columna1
df['columna1'].hist()
# Agregar etiquetas al gráfico
plt.title('Histograma de columna1')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
# Mostrar el gráfico
plt.show()


def custom_max(n1: int, n2: int):
    """
    The custom_max function takes two numbers as input and returns the larger of the two.

    :param n1: int: Define the first number that will be used in the function
    :param n2: int: Specify the type of data that is expected to be passed into the function
    :return: The maximum value of n3
    :doc-author: Trelent
    """
    return n1


def custom_vision(a: int, message=None):
    """

    Args:
        a: primer numero
        message: mensaje a retornar

    Returns:
        mensaje: dsff
    """
    return message
