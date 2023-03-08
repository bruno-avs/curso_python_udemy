from itertools import zip_longest

cidades = ['são paulo', 'rio de janeiro', 'belo horizonte', 'amapa']
estados = ['sp', 'rj', 'mg ']

city_estates = zip_longest(estados, cidades, fillvalue='estado')

print(city_estates)
for iter in city_estates:
    print(iter)
