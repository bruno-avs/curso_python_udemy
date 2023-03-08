from modules.cnpj_functions import check_sequence, format_cnpj, create_file_with_cnpjs
from digit_generator import generate_cnpj
from random import randint

print('Por favor nos informe a baixo quantos CNPJs deseja gerar.')

quantity_to_be_generated = input(': ')
quantity_to_be_generated.strip()

if quantity_to_be_generated.isnumeric():
    cnpjs_to_be_generated = int(quantity_to_be_generated)

    cnpjs_generated = []

    print('Gerando......')

    while cnpjs_to_be_generated > 0:
        ramdom_number = str(randint(10000000, 99999999)) + '0001'

        if not check_sequence(ramdom_number):
            generated_cnpj = generate_cnpj(ramdom_number)
            cnpj_formatted = format_cnpj(generated_cnpj)

            cnpjs_generated.append(cnpj_formatted)

            print(f'\t{cnpj_formatted}')

            cnpjs_to_be_generated -= 1

    create_file_with_cnpjs(cnpjs_generated)