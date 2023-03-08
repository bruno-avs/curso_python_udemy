def calculate_digit(mult_result):
    formula_result = 11 - (mult_result % 11)
    return formula_result if formula_result <= 9 else 0

def check_sequence(numbs_cnpj):
    sequencia = numbs_cnpj[0] * len(numbs_cnpj)

    if sequencia == numbs_cnpj:
        return True
    return False

def format_cnpj(generated_cnpj):
    cnpj_formatted = ''
    for index, number in enumerate(generated_cnpj):
        if index == 2 or index == 5:
            cnpj_formatted += '.' + number
            continue
        if index == 8:
            cnpj_formatted += '/' + number
            continue
        if index == 12:
            cnpj_formatted += '-' + number
            continue
        cnpj_formatted += number

    return cnpj_formatted

def create_file_with_cnpjs(cnpjs):
    with open('cnpj_gerados', 'w+') as file:
        file.write(f'CNPJs gerados:\n')
        for cnpj in cnpjs:
            file.write(f'\t{cnpj}\n')

