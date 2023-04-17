import pybase64 as base
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

# Leer archivo en formato binario
with open('prueba.jpg', 'rb') as file:
    archivo = file.read()
# Codificar archivo a base 64

contenido_codificado = base.b64encode(archivo)
print(contenido_codificado)
# Decodifica el contenido de la imagen en Base64
contenido_decodificado = base.b64decode(contenido_codificado)
# Guarda el contenido decodificado en un archivo nuevo
with open("imagen_decodificada.jpg", "wb") as archivo:
    archivo.write(contenido_decodificado)
# Publicar imagen
image = mpimg.imread('imagen_decodificada.jpg')
plt.imshow(image)
plt.show()