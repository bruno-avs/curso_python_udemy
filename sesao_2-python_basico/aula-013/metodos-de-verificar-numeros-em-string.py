"""
Métodos que verificam se uma string pode ser convertida em um numero inteiro
"""
num_1 = input('Digite um número. ')
num_2 = input('Digite outro. ')

# os tres métodos a sequir verificam se uma string possue só números inteiros positivos
# Retornando um boolean

is_number_1 = num_1.isdecimal()
is_number_2 = num_2.isdecimal()

is_number_3 = num_1.isnumeric()
is_number_4 = num_2.isnumeric()

is_number_5 = num_1.isdigit()
is_number_6 = num_2.isdigit()

if is_number_1 and is_number_2:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 * num_2)
except:
    print('Erro')







