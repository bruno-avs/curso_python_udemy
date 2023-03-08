"""
Entrada de dados
"""
quest_nome = 'Qual é o seu nome? '
quest_idade = 'Qual é a sua idade? '
quest_numero1 = 'Escolha um número: '
quest_numero2 = 'Escolha outro número: '

nome = input(quest_nome)
idade = input(quest_idade)

print(f'Ola!! {nome}, vamos fazer ums calculos.')

numero_1 = int(input(quest_numero1))
numero_2 = int(input(quest_numero2))
resultado = numero_1 + numero_2

print(f'O resultado da operação é: {resultado}')

