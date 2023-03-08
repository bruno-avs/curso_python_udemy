user_cpf = input('Digite o seu CPF para fazermos a validação ex(000.000.000-00): ')
lista = [True, False]
lista.sort(reverse=True)
print(lista)
try:
    user_cpf = user_cpf.strip()

    cpf = user_cpf.split("-")
    last_2_nums = cpf[1]
    the_first_9_nums = "".join(cpf[0].split("."))

    first_total = 0
    for key, multi in enumerate(range(10, 1, -1)):
        first_total += int(the_first_9_nums[key]) * multi

    first_equation_res = 11 - (first_total % 11)
    first_digit = 0 if first_equation_res > 9 else first_equation_res

    cpf_numbers = the_first_9_nums + last_2_nums
    its_a_sequence = cpf_numbers == str(first_digit) * 11

    if str(first_digit) == last_2_nums[0] and not its_a_sequence:
        second_mult_nums = the_first_9_nums + str(first_digit)

        second_total = 0
        for key, multi in enumerate(range(11, 1, -1)):
            second_total += int(second_mult_nums[key]) * multi

        second_equation_res = 11 - (second_total % 11)
        second_digit = 0 if second_equation_res > 9 else second_equation_res

        if str(second_digit) == last_2_nums[1]:
            print("O CPF é valido.")
        else:
            print("CPF invalido!!!!.")

    else:
        print("CPF invalido!!!!.")

except:
    print("CPF invalido!!!!.")
