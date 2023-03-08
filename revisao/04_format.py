"""
referencias:
https://www.w3schools.com/python/ref_string_format.asp
https://cienciaprogramada.com.br/2022/03/formatacao-strings-python/#Metodo_format

O método format permite inserir e valores em uma string
usado um marcador de posição {}
"""
texto = "Ola {} {} seja bem vindo."
name = "bruno"
last_name = "alves"

"""Você pode inserir os valores de forma sequencial"""
print(texto.format(name.title(), last_name))
print("-" * 40)

"""Você também pode inserir os valores usando index [0] [-1]"""
texto_2 = "Ola meu nome é {0}, e tenho {1} anos.".format(name, 20)
print(texto_2)
print("-" * 40)

"""outra forma é usando parâmetros nomeados"""
texto_3 = "Ola meu nome é {name}, " \
    "e tenho {old} anos.".format(name="João", old=30)
print(texto_3)
print("-" * 40)
