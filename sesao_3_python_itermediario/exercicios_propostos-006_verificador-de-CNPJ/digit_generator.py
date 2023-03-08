def calculate_digit(mult_result):
    formula_result = 11 - (mult_result % 11)
    return formula_result if formula_result <= 9 else 0

def check_sequence(numbs_cnpj):
    sequencia = numbs_cnpj[0] * len(numbs_cnpj)
    if sequencia == numbs_cnpj:
        return True

    return False

def validate_cnpj(numbs_cnpj, digits):
    multiplier = 5
    counter = 0
    generated_digits = 0

    mult_result_one = 0
    mult_result_two = 0
    first_digit = 0

    while True:
        if multiplier < 2:
            multiplier = 9

        if generated_digits == 0:
            mult_result_one += int(numbs_cnpj[counter]) * multiplier

            if counter == 11:
                first_digit = calculate_digit(mult_result_one)
                generated_digits += 1
                counter = 0
                multiplier = 6

        if generated_digits == 1:

            if str(first_digit) == digits[0]:
                new_numbs_cnpj = numbs_cnpj + str(first_digit)
                mult_result_two += int(new_numbs_cnpj[counter]) * multiplier

                if counter == 12:
                    second_digit = calculate_digit(mult_result_two)
                    calculated_digits = str(first_digit) + str(second_digit)

                    if calculated_digits == digits:
                        print('CNPJ valido!!!.')

                    else:
                        print('CNPJ invalido!!!.')
                    break
            else:
                print('CNPJ invalido!!!.')
                break

        multiplier -= 1
        counter += 1