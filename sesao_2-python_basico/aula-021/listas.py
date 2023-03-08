"""
Listas em python
"""
# listas possuem tamben índices negativos

# você pode recortar uma lista usado indices [inicio: fim : passos]
lista_1 = [1,2,True, 1.2, "ola", 10]
new_list = lista_1[1:3]
print(new_list)
print()

# assim vc inverte uma lista
print(lista_1[::-1])
print()

# È possivel concatenar uma lista comm outra lista
lista_2 = ["+", 1,2,3,12]
print(lista_1 + lista_2) # com o operador de adição

lista_1.extend(lista_2) # com o método extend
print(lista_1)
print()

# métodos para listas
lista_one = [1,2, True, False, "c"]
print(lista_one)
lista_one.append(1)  # adiciona um valor ao final da lista
print("lista_one.append(1)", lista_one, sep=" => ")

lista_one.insert(0, "adicionado")  # adiciona um valor no index informado
print(f"lista_one.insert(0, 'adicionado') => {lista_one}")

lista_one.pop(3)  # por padrão deleta o ultimo valor de uma lista.
# voce pode passar um index caso queira deletar um outro item
print(f'lista_one.pop(3) => {lista_one}')

del(lista_one[0:2])  # del deleta valores
print(lista_one)

max(1,2,3)  # retorna o maior valor
min(1,2,3)  # retorna o menor valor

list_2 = list("Ola meu nome é bruno")  # cria uma lista com um elemento iteravel
print(list_2)





