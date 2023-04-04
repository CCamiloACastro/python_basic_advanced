balance = 499

if __name__ == '__main__':
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



