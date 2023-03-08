from data import products, people

maior_de_idade = filter(lambda x: x['old'] >= 40, people)
produtos_maior_que_10 = filter(lambda x: x['value'] > 40, products)

for pesseoa in maior_de_idade:
    print(pesseoa)
print('#' * 30)
for produtos in produtos_maior_que_10:
    print(produtos)