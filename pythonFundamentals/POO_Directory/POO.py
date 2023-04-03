"""Las clases proporcionan un medio para agrupar datos y funcionalidad. La creación de una nueva clase crea un nuevo
tipo de objeto, lo que permite crear nuevas instancias de ese tipo. Cada instancia de clase puede tener atributos
adjuntos para mantener su estado. Las instancias de clase también pueden tener métodos (definidos por su clase) para
modificar su estado.
Terminología
Se define de esta forma UpperCamelCase
Instancia: El objeto que es creado al llamar una clase
Atributo de una clase: Propiedad que tendrían todas las instancias
Método: Función que existe de una clase
"""


class Restaurant:

    # __init__(self): Es un constructor que se ejecuta automáticamente sin tener que llamarlo
    # Un constructor es una función única que se llama automáticamente cuando se crea un objeto de una clase.
    # El objetivo principal de un constructor es inicializar o asignar valores a los miembros de datos de esa clase.
    # No puede retornar ningún valor que no sea None.

    # Cualquier atributo que se agregue en init se tiene que colocar al momento de instanciarlo
    def __init__(self, name, category, price):
        # None es frecuentemente usado para representar la ausencia de valor (vacío)
        self.years_business = None
        self.name = name
        self.category = category
        self.price = price

    # self: ofrece un modo de cálculo para hacer referencia al contenido del objeto con el que está asociado sin
    # tener que hacer referencia explícitamente al objeto.
    def add_restaurant(self, nombre):
        print('Agregando...')
        self.name = nombre
        print(f'Agregado')

    def show_information(self):
        print(f'\t{self.name} \nCategoria: {self.category}\nPrecio: {self.price}')


# Instanciar la clase
restaurant = Restaurant('Tamales uyuy','Comida tolimense', 50)
# print(restaurant.name)
restaurant.add_restaurant('Tamales uyuyuy')
# print(restaurant.name)

restaurant2 = Restaurant('Pizzeria uyuyuy','Comida rapida',20)

restaurant.show_information()
restaurant2.show_information()
