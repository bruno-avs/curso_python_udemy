lista_de_comprar = []

lista_de_comprar.append(('calça', 100))
lista_de_comprar.append(('bermuda', 55))
lista_de_comprar.append(('blusa', 30))
lista_de_comprar.append(('tenis', 80))

soma_valores = sum([v[1] for v in lista_de_comprar])

print(f'Sua compra deu um total de {soma_valores}R$ reais.')