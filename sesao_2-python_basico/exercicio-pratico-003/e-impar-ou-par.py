number = input('Por favor digíte um número inteiro: ')

is_number = number.isnumeric()

if is_number:
    number = int(number)
    splited_number = number % 2
    if splited_number == 0:
        print(f'O número {number} é par.')
    else:
        print(f'O número {number} é impar.')