"""
Una funcion es un bloque de codigo diseñado para relaizar una actividad

def nombrefuncion():

funcion
"""


def calculate_numbers(a, b):
    print(f'los numeros ingresados son: {a} y {b}')
    print(f'Suma {a+b}')
    print(f'Resta {a-b}')
    print(f'Multiplicacion {a*b}')
    print(f'Division {a/b}')
    print(f'Potencia {a**b}')
    print(f'Modulo {a % b}')
    print(f'Division entero {a // b}')


def information(name, ocupation='unknown ocupation'):
    return f'soy {name} y soy {ocupation}'


def operators_bit_bit(a, b):
    print(f'Funcion AND {a & b}')
    print(f'Funcion OR {a | b}')
    print(f'Funcion XOR {a ^ b}')
    print(f'Funcion NOT {~a}')
    print(f'Funcion desplazamiento der {a >> b}')
    # Realiza un desplazamiento a la derecha bit a bit.
    # Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha
    print(f'Funcion desplazamiento der {a << b}')
    # Realiza un desplazamiento a la izquierda bit a bit. Desplaza
    # los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha



if __name__ == '__main__':
    calculate_numbers(45, 12)
    print(information('name1', 'estudiante'))
    print(information('name2'))
    operators_bit_bit(3,3)

