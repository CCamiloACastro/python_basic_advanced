import pandas as pd

data= {'name':['Miguel','Mario','Pedro','Lucy'],
         'age':[32,45,38,43],
         'city':['Medellin','Bogota','San Andres', 'Pasto']
         }
#Actualizar
data.update({'age':[28,32,11,22]})
print(data)
#Eliminar datos
#data.pop('city')
print(data)
#Limpiar dataframe
#data.clear()
df = pd.DataFrame(data)
print(df)


