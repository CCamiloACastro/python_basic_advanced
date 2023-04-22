import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
# Cargar los datos desde el archivo de Excel
df = pd.read_excel('./ds_salaries.xlsx')

# Transformar la variable job_title en una variable numérica
le = LabelEncoder()
df['job_title_num'] = le.fit_transform(df['job_title'])

# Seleccionar las características a utilizar en el clustering
X = df[['job_title_num', 'salary_in_usd']].values

# Entrenar el modelo de clustering con KMeans
kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(X)

# Obtener los centroides y las etiquetas de cada punto
centroides = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualizar los resultados
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
plt.title('KMeans Clustering')
plt.xlabel('job_title')
plt.ylabel('salary_in_usd')
plt.show()

# Evaluar los modelos con los datos de prueba
print("Resultados de KMeans:")
print(kmeans.predict(X))
