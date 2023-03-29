name = input('Cual es tu nombre de usuario: \r\n')
print(f'Bienvenido {name}')

nivel = input('Cual es tu nivel de usuario: \r\n')
nivel = int(nivel)

if nivel >= 100:
    print('ya eres un master')
else:
    print('Sigue jugando')
