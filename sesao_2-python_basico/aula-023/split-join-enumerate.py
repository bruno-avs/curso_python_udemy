"""
str.split("") => retorna uma lista contendo os elementos separados de acordo
                 com o separador passado como argumento.

"".join(list) => retorna uma string com os elementos de uma lista concatenados

enumerate() => enumera elementos de uma lista

"""
string = "Ola meu nome è bruno"
print(string)
string_splited= string.split(" ")
print(string_splited)

string_concate = ", ".join(string_splited)
print(string_concate)

lista = ["ola", "ola", "jaj"]
for enum, valor in enumerate(lista):
    print(enum,valor)

enumerada = list(enumerate(lista))
print(enumerada)
