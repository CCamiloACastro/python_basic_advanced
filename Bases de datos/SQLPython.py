import pandas as pd
from sqlalchemy import create_engine  # (pip install --upgrade 'sqlalchemy<2.0’)

# create_engine('tipo_de_base_de_datos://usuario:contraseña@host:puerto/base_de_datos')
conn = create_engine('mysql+pymysql://root:1234567890@localhost:3306/repositorio')
# Ejecutar un query (1)
df = pd.read_sql("SELECT * FROM usuario", conn)
print(df)

"""
When a user who doesn’t exist on the MySQL server tries to access the database.
When there is no privilege for the user.
If the username or password is wrong.
"""