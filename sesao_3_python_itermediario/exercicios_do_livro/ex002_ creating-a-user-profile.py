print(
    'Vamos criar um perfil de usuario pra você.'
    ' Por favor nos informe seus dados abaixo.'
)

name = input('Iforme o seu nome: ')
lart_name = input('Informe o seu sobrenome: ')
add_more_info = input('Deseja adicionar mais alguma informação (sim ou não)? ')

accepted_words = ('n', 'nao', 'não')

questions = [
    'Quantos anos você tem? ',
    'Qual é o seu estado cívil? ',
    'Tem filhos? ',
    'Qual é a sua música favorita? '
]

counter = 0
extra_user_information = []
dont_want_to_inform = add_more_info not in accepted_words

while dont_want_to_inform:
    if counter >= len(questions): break

    input_info = 'Digite (não) para terminar.\n'
    user_information = input(input_info + questions[counter])

    if user_information in accepted_words: break

    extra_user_information.append(user_information)

    if len(extra_user_information[counter]) == 0:
        extra_user_information[counter] = 'Não informado'

    counter += 1

def creat_user(name, second_name, key_values, *args):
    person = {}
    person['name'] = name
    person['second name'] = second_name
    person['full name'] = f'{name} {second_name}'

    for key, information in enumerate(args):
        person[key_values[key]] = information
    return person

key_values = ['idade', 'estado civil', 'possui filhos', 'música favorita']
new_user = creat_user(name, lart_name, key_values, *extra_user_information)

print(new_user)
