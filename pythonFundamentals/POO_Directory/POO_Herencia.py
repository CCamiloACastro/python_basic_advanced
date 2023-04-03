class Restaurant:

    def __init__(self, name, category, price):
        self.name = name  # Public
        self._category = category  # Protected
        self.__price = price  # Private
        self.__location = 'Bogota'

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


# Crear una clase hijo de Restaurant
class Hotel(Restaurant):

    # El init es de esta clase mientras que Super().init hace referencia al padre
    def __init__(self, name, category, price):
        super().__init__(name, category, price)



hotel = Hotel('Hotel BumBum', '5 estrella', 200)
hotel.show_information()
