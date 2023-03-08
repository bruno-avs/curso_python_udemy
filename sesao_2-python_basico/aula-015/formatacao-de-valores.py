number = input('Digite um número: ')
name = input('Digite o seu nome: ')

name_lower = name.lower()
name_upper = name.upper()
name_title = name.title()

print(f'{int(number):.2f}') # colocando um número com mais de uma casa decimal
print(f'Nome todo em letras minusculas {name_lower:#^20s}\n'
      f'Nome todo em letras maiusculas {name_upper:$>20s}\n'
      f'Nome só com as letras iniciais em maiuscula {name_title:%<20s}')
