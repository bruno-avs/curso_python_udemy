name = input('Digite seu nome: ')
current_hors = input('Qua é a hora atual? ')

is_valid = current_hors.isdecimal()

if is_valid:
    hors = int(current_hors)
    if hors > 0 and hors < 5:
        print(f'Boa madrugada {name}, parece que não esta consequindo dormir. ')
    elif hors < 13:
        print(f'Bom dia {name}!!!!. ')
    elif hors < 18:
        print(f'Boa tarde {name}!!!!. ')
    else:
        print(f'Boa noite {name}!!!')