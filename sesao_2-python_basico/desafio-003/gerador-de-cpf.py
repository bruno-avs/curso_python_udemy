from random import randint

random_nums = str(randint(100000000, 999999999))

generated_cpf = random_nums

reverse = 10
total = 0

for key in range(19):
    if key > 8:
        key -= 9

    total += int(generated_cpf[key]) * reverse
    reverse -= 1
    if reverse < 2:
        digit = 11 - (total % 11)
        if digit > 9:
            digit = 0
        generated_cpf += str(digit)
        reverse = 11
        total = 0

first_9_digits = [
    generated_cpf[0:3],
    generated_cpf[3:6],
    generated_cpf[6:9]
]
cpf = ".".join(first_9_digits)
cpf += "-" + generated_cpf[-3: -1]
print(cpf)
