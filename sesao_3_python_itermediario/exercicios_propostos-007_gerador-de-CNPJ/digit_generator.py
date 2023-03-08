from modules.cnpj_functions import calculate_digit

def generate_cnpj(numbs_cnpj):
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

            if counter >= 11:
                first_digit = calculate_digit(mult_result_one)
                generated_digits += 1
                counter = 0
                multiplier = 6

        if generated_digits == 1:
            new_numbs_cnpj = numbs_cnpj + str(first_digit)
            mult_result_two += int(new_numbs_cnpj[counter]) * multiplier

            if counter >= 12:
                second_digit = calculate_digit(mult_result_two)
                return numbs_cnpj + str(first_digit) + str(second_digit)

        multiplier -= 1
        counter += 1
