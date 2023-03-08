class Caneta:
    def __init__(self, marca, preco, cor):
        self.marca = marca
        self._preco = preco
        self.__cor = cor


caneta = Caneta('BIC', 'R$ 2,00', 'vermelha')
print(caneta.marca) ## esta é uma propriedade publica
print('#'*8)
print()
print(caneta._preco) ## esta é uma popriedade protegida
print('#'*8)
print(caneta._Caneta__cor) ## esta é uma propriedade privada, perceba que o python renomeia a
# propriedade para dificultar o acesso da mesma
