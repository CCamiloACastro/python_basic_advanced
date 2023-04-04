"""
Hay dos formas de llamar los getters y setters

get_variable
o
@ property
def variable()
"""


class Restaurant:

    def __init__(self, name, category, price):
        self.name = name  # Public
        self._category = category  # Protected
        self.__price = price  # Private
        self.__location = 'Bogota'

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def add_restaurant(self, nombre):
        print('Agregando...')
        self.name = nombre
        print(f'Agregado')

    def show_information(self):
        print(f'\t{self.name} \nCategoria: {self._category}\nPrecio: {self.__price}')


# Instanciar la clase
restaurant = Restaurant('Tamales uyuy', 'Comida tolimense', 50)

print(restaurant.name)  # Public: Puede ser accedido
print(restaurant._category)  # protected: Puede ser accedido pero no se recomienda
# print(restaurant.__price) # No se puede acceder
# AttributeError: 'Restaurant' object has no attribute '__price'

# Para acceder se hace por medio de los getter and setters
# Método 1
print(restaurant.get_price())
restaurant.set_price(30)
print(restaurant.get_price())

# Método 2
print(restaurant.location)
restaurant.location = 'Medellin'
print(restaurant.location)
