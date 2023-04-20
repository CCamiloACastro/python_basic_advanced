Flet requires Python 3.7 or above. To start with Flet, 
you need to install flet module first:

Para comprobar la version de python
`python --version`

Instalar modulo `pip install flet`

Actualizar modilo `pip install flet --upgrade`

La guia de inicio esta en [Flet Docs](https://flet.dev/docs/guides/python/getting-started)


_Internamente, cada aplicación de Flet es una aplicación web e incluso si se abre 
en una ventana nativa del sistema operativo, un servidor web incorporado aún se 
inicia en un segundo plano. El servidor web Flet se llama "Fletd" y, de forma 
predeterminada, escucha en un puerto TCP aleatorio. Puede especificar un puerto 
TCP personalizado y luego abrir la aplicación en el navegador junto con la vista 
de escritorio:_

`flet.app(port=8550, target=main)`

En el navegador sería así `http://localhost:<port>`