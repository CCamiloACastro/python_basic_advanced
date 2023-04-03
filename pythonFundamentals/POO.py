"""Las clases proporcionan un medio para agrupar datos y funcionalidad. La creación de una nueva clase crea un nuevo
tipo de objeto, lo que permite crear nuevas instancias de ese tipo. Cada instancia de clase puede tener atributos
adjuntos para mantener su estado. Las instancias de clase también pueden tener métodos (definidos por su clase) para
modificar su estado.
Terminología
Se define de esta forma UpperCamelCase
Instancia: El objeto que es creado al llamar una clase
Atributo de una clase: Propiedad que tendrían todas las instancias
Método: Función que existe de una clase

Construnctor: Es una función que se ejecuta automaticamente al crear un nuevo objeto por medio de una clase
"""


class Restaurant:
    # __init__(self): Es un constructor que se ejecuta automaticamente sin tener que llamarlo
    # Cualquier atributo que se agregue en init se tiene que colocar al momento de instanciarlo
    def __init__(self, category):
        # None es frecuentemente usado para representar la ausencia de valor
        self.nombre = None
        self.category = category
        print('me ejecuto automáticamente')

    # self: ofrece un modo de cálculo para hacer referencia al contenido del objeto con el que está asociado sin
    # tener que hacer referencia explícitamente al objeto.
    def add_restaurant(self, nombre):
        print('Agregando...')
        self.nombre = nombre
        print(f'Agregado {self.nombre}')

    def show_information(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.category}')


# Instanciar la clase
restaurant = Restaurant('Comida tolimense')
restaurant.add_restaurant('Tamales uyuy')

restaurant2 = Restaurant('Comida rapida')
restaurant2.add_restaurant('Pizzeria uyuy')

restaurant.show_information()
restaurant2.show_information()
