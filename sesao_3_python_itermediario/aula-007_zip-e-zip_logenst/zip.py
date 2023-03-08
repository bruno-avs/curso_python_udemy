cidades = ['são paulo', 'rio de janeiro', 'belo horizonte']
estados = ['sp', 'rj', 'mg ']

cidades_estados = zip(iter(cidades), iter(estados))

di = dict(cidades_estados)
print(di)




