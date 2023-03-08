nome = input('Qual é o seu nome? ')

nome_len = len(nome)

if nome_len <= 4:
    print('Seu nome é pequeno.')
elif nome_len <= 6:
    print('Seu nome é normal.')
else:
    print('seu nome é muito grande.')