nome = input('Por favor, poderia nos informar o seu nome? ')
idade = int(input('Poderia nos informar a sua idade tambem '))

print(f'Ola {nome} estamos analizando seu dados.')

if idade < 16:
    print(f'{nome}, infelismente você não pode votar ainda.')
elif idade < 18:
    print(f'{nome}, você ja pode votar, seu voto ainda não é obrigatório.')
elif idade < 60:
    print(f'{nome}, você pode votar, seu voto é obrigatório.')
else:
    print(f'{nome}, o senho pode votar, mais seu voto não é mais obrigatório.')