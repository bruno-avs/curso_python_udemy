# convertendo valores em um set
tupla = (1,3,4,4)
lista = [1,3,4,4]
dicionario = {
    'name':'bruno',
    'lat name':'alves'
}
var = 'buno'

sets1 = set(tupla)
sets2 = set(lista)
sets3 = set(dicionario)
sets4 = set(var)

print(sets1)
print(sets2)
print(sets3)
print(sets4)
print()
# adicionando valore em um set
sets1.add(12)
print(sets1)
print()
# removendo valores
r = sets1.discard(1)  # não a retorno
print(r)
print(sets1)
print()
# adiciona valore a um set
sets1.update('ol')
print(sets1)


