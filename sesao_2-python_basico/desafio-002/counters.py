print("Digite números positivos de 0 a 100: ")
progre_value = input('Digite um número para contagem progressiva: ') or "0"
progre_limit = input('Digite um número para o fim da contagem (não pode ser 0): ') or "10"

regre_value = input("Digite um número para contagem regressiva (não pode ser 0): ") or "10"
regre_limit = input('Digite um número para o fim da contagem: ') or "0"

progre_is_number = progre_value.isnumeric()
progre_limit_is_number = progre_limit.isnumeric()

regre_is_number = regre_value.isnumeric()
regre_limit_is_number = regre_limit.isnumeric()

all_numbers = progre_is_number and progre_limit_is_number and regre_is_number and regre_limit_is_number

if all_numbers:
    progre_value = int(progre_value)
    progre_limit = int(progre_limit)
    regre_value = int(regre_value)
    regre_limit = int(regre_limit)

    is_greater_than_zero = progre_limit > 0 and regre_value > 0
    is_less_than_a_hundred = progre_limit < 100 and regre_value < 100

    if is_greater_than_zero and is_less_than_a_hundred:
        counter_progre = progre_value
        counter_regre = regre_value

        print("progresiva    regressiva")

        while counter_progre <= progre_limit and counter_regre >= regre_limit:
            if counter_progre <= progre_limit:
                print("  ", counter_progre, end="       |       ")
            if counter_regre >= regre_limit:
                print(counter_regre)
            counter_progre += 1
            counter_regre -= 1
    if not is_greater_than_zero:
        print("Por favor digite valores acima de 0.")
    if not is_less_than_a_hundred:
        print("Por favor digite valores menores que 100.")


