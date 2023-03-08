name_dataBase = "Bruno"
key_dataBase = "1234567"

wat_to_enter = input('Ola!!, seja bem vindo ao sistema, deseja fazer o login? ')

if "sim" in wat_to_enter or "yes" in wat_to_enter:
    print('Então vamos la, poderia nos informar o seu nome de usuario e senha por favor. ')

    name = input('Nome de usuario: ')

    if name == name_dataBase:
        key = input('Senha: ')
        if key == key_dataBase:
            print('Ola!! {}, você esta logado no nosso sistema.'.format(name))
        else:
            print('Ops, senha invalida!.')
    else:
        print('Nome de usuario invalido!.')

else:
    print('Obrigado por usar nossos serviços até breve.')



