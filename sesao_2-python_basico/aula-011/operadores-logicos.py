"""
operadores lógicos
and(e), or(ou), not(não), in(esta), not in(não esta)
"""
number_1 = 4
number_2 = 5
number_3 = 9
number_4 = 2

nome = "bruno alves"

if number_1 < number_2 and number_3 > number_4:
    print('executei')

if number_1 >= number_3 or number_4 <= number_2:
    print('executei')

if not False:
    print('executei')

if "alves" in nome:
    print('executei')

if "sdsad" not in nome:
    print('executei')