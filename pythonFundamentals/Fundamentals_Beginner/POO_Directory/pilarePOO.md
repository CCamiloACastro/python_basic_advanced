# Pilares de la programación orientada a objetos

## Abstracción
Son los datos necesarios de una clase. Cuando se hace una abstracción, 
se quiere **omitir detalles** que no son necesarios para la clase, y se quiere 
solamente mostrar lo que sí es **relevante**.

## Encapsulamiento
Permite restringir u ocultar el acceso a  los datos dentro de la misma clase 
del mundo exterior (usualmente se modifica mediante métodos de la misma clase)

La idea es no poder modificar variables si no es por métodos

`restaurant.nombre = 'Tamales uyuyuy'` <-- Esto NO!

## Herencia
Se puede crear una clase que sea hijo o una copia de otra, al heredar una 
clase se tienen todos los métodos y atributos de la clase padre en el hijo,
y se puede modificar en caso de que sea necesario

## Polimorfismo
Es la habilidad de tener diferentes comportamientos basados en que subclase se
está utilizando, relacionado muy estrechamente como herencia.

Básicamente, es cuando se hereda de una clase superior pero se puede modificar
métodos, variables...