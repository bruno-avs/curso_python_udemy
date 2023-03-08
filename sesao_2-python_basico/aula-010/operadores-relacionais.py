"""
Operadores relacionais
== <= < >= > !=
"""
nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))

idade_limite = 18

if idade >= idade_limite:
    print(f'Ola {nome}, verificamos que você é maios de idade, podera votar.')
else:
    print(f'Ola {nome}, verificamos que você ainda é menor de idade, não podera votar.')

