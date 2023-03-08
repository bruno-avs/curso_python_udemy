"""
Referencias.
https://www.w3schools.com/python/ref_func_zip.asp
https://realpython.com/python-zip-function/
https://www.programiz.com/python-programming/methods/built-in/zip
"""
# A função zip faz basicamente o emparelhamento dos valores de dois ou mais
# iteráveis, ele pega o primeiro valor (index 0) de cada iterável e os junta
# em uma tupla, depois pega o segundo valor de cada iterável e junta-os em
# uma tupla e assim sucessivamente até que o index final do iterável com
# menos index for iterado
# zip retorna um objeto zip que é um iterador

iteravel_1 = [1, 2, 3, 4, 5, 6]
iteravel_2 = ["bruno", "João", "mateus", "lucas"]

zipper = zip(iteravel_1, iteravel_2)

dict_zip = {}
for it_1, it_2 in zipper:
    dict_zip[it_2] = it_1

print(dict_zip)
