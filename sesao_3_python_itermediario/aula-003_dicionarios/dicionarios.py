dic = {
    'name': 'bruno',
    'last name': 'alves',
    'old': 20,
}
dic2 = {
    'name': 'josé',
    'last name': 'henrique',
}

ret = dic.popitem()  # retira o ultimo item de um dicionario
print(ret)
print(dic)
print()

outer = dic.pop('last name')  # retira do dicionario o item especificado
print(outer)
print(dic)
print()

new_dictionary = dic.update(dic2)  # concatena dicionarios
print(new_dictionary)

