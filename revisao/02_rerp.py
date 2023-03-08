"""
referencias: 
    https://www.programiz.com/python-programming/methods/built-in/repr
    https://pt.stackoverflow.com/questions/201701/afinal-para-que-serve-a-fun%C3%A7%C3%A3o-repr-no-python"""

"""O método repr, permite a conversão de um objeto em string"""

"""Ele se difere de str, pois str é voltado para exibir a saída para o
usuário já repr é focado em gerar uma saída para a maquina"""
content = 2 * 4 / 90
string = repr("ola")
cont_repr = repr(content)
print(cont_repr)
print(string)

"""
A maior utilidade de repr é que você pode mudar a forma como ele representa 
os valores a partir do Dudley method dele
"""
