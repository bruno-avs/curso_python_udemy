from itertools import zip_longest

"""
Referencias
https://acervolima.com/python-itertools-zip_longest/
https://blog.teclado.com/python-zip_longest/
"""
iteravel_1 = [10, 9, 2, 45, 30]
iteravel_2 = ["bruno", "João", "mateus", "lucas"]
# A função zipper_longest é quase idêntica a função embutida zip
# ela pega todos os valores dos index 0 dos iteráveis passados a ela como
# argumento e os junta em uma tupla fazendo isso para todos os index
# a diferença é que esta permite definir um valor padrão para ser usado quando
# quando um iterável for menor que o outro, diferente de zip que apenas ignora
# os valores que passa do máximo que é definido com base no iterável com
# menor comprimento

zipper = zip_longest(iteravel_1, iteravel_2, fillvalue="Desconhecido")

zipper_dict = {}
for iter_1, iter_2 in zipper:
    zipper_dict[iter_2] = iter_1

print(zipper_dict)
