# Constructor 

Un constructor es una función única que se llama automáticamente cuando 
se crea un objeto de una clase.
El objetivo principal de un constructor es inicializar o asignar valores a 
los miembros de datos de esa clase. 
No puede devolver ningún valor que no sea None.

## Sintaxis

`def __init__(self):
	# initializations`

## Tipos de constructores en Python 

* Constructor parametrizado:

Tiene parámetros que se inicializan cuando sé instancia el objeto
`def __init__(self,n1,n2,...,n)`
* Constructor no parametrizado 

No tiene parámetros que se inicializan cuando sé instancia el objeto
`def __init__(self,n1,n2,...,n)`
* Constructor predeterminado

Python mismo crea un constructor durante la compilación del programa.
El constructor está vacío, osea no tiene código adentro
