from digit_generator import validate_cnpj, check_sequence
print('Por favor nos informe a baixo o número do seu CNPJ.')

while True:
    input_cnpj = input('CNPJ: ')
    input_cnpj.strip()

    splited_cnpj = input_cnpj.split('-')

    if len(splited_cnpj) == 2:
        numbs_cnpj = splited_cnpj[0].replace('.', '').replace('/', '')
        digits = splited_cnpj[1]
        all_numbers = numbs_cnpj.isnumeric() and digits.isnumeric()

        if not  all_numbers or check_sequence(numbs_cnpj):
            print('O CNPJ informado não pode ser analisado.')
            continue
    else:
        print('O CNPJ informado não pode ser analisado.')
        continue
    validate_cnpj(numbs_cnpj, digits)

