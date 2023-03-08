"""
caulculadora com while
"""
# forma 01

while True:
    number_1 = input('Digite um número: ')
    number_2 = input('Digite outro número: ')
    operator = input('Digite um operador: ')

    if not number_1.isdecimal() or not number_2.isdecimal():
        print('Por favor digite um número')
        continue

    number_1 = int(number_1)
    number_2 = int(number_2)

    result_template = f'entre {number_1} e {number_2} é ='

    if operator == "+":
        soma = number_1 + number_2
        print(f'A soma {result_template} {soma}.')
    elif operator == "-":
        sub = number_1 - number_2
        print(f'A subritação {result_template} {sub}.')
    elif operator == "/":
        div = number_1 / number_2
        print(f'A divisão {result_template} {div}.')
    elif operator == "*":
        mult = number_1 * number_2
        print(f'A multiplicação {result_template} {mult}')
    else:
        print("Operador invalido")

    out = input('Deseja sair: [s] sim [n] não ')
    if out == 's':
        break



