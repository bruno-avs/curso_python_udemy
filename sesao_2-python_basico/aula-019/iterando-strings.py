user_text = input('Digite um texto: ')
str_mas_len = len(user_text)


if not user_text.isnumeric() and str_mas_len != 0:
    counter = 0
    new_str = ''

    upper_value = input('Agora digite o a letra que deseja por em maiúsculo: ')

    if not upper_value.isdigit() and len(upper_value) != 0:
        while counter < str_mas_len:
            curr_str = user_text[counter]
            counter += 1
            if curr_str == upper_value:
                new_str += curr_str.upper()
            else:
                new_str += curr_str

        print(new_str)
    else:
        print('Por favor digite uma letra!!!.')
else:
    print('Por favor digite um texto valido.')