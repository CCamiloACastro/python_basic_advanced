balance = 499


if balance == 500:
    print('Estas en el limite')
if balance > 500:
    print('Eres multimillonario')
if balance < 500:
    print('Trabaje!!')
if balance >= 500:
    print('Sigue asi')
if balance <= 500:
    print('Trabaja tu puedes!!')
if balance != 500:
    print('Entonces..¿Cuanto ganas?')

if balance < 500:
    print('Eres pobre')
elif balance == 500:
    print('Estas en el limite')
else:
    print('Puedo ser tu amigo?')

usuario = True
administrador = True
if usuario and administrador:
    print('logueado administrador')
elif usuario or administrador:
    print('usuario logueado')
else:
    print('DEbes iniciar sesión')

languages = ['español', 'ingles', 'aleman', 'japones', 'italiano', 'vietnamita', 'chibcha']

for language in languages:
    print(language)
    if len(language) > 7:
        print('nombre largo')
    else:
        print('nombre corto')

# match statement

"""
Una declaración de coincidencia toma una expresión y compara su valor con patrones sucesivos dados como uno o más 
bloques de casos.
Similar a un switch
Solo se ejecuta el primer patrón que coincide y también puede extraer componentes (elementos de secuencia o 
atributos de objeto) del valor en variables.
"""

# Ejemplo 1
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 403 | 404:
            # "|" "or"
            return "Not allowed"
        case _:
            # El “nombre de la variable” _ actúa como un comodín y nunca deja de coincidir.
            # Si ningún caso coincide, ninguna de las ramas se ejecuta
            return "Something's wrong with the internet"

# Ejemplo 2

from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

# Ejemplo 3

class Point:
    x: int
    y: int


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point(x, y) if x == y:
            # El "if" es conocido como "guardia".
            # Si la guardia es falsa, el match continúa para intentar el siguiente bloque de caso.
            # El valor se captura antes de que se evalúe el guardia
            print(f"Y=X at {x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")