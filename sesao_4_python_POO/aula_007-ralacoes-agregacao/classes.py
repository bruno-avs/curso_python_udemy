class CarinhoCompras:
    def __init__(self):
        self.__carinho = []

    def add_produto(self, produto):
        self.__carinho.append(produto)
    def listar_produtos(self):
        for produto in self.__carinho:
            print(produto.tipo, produto.preco)
    def total(self):
        total = 0
        for produto in self.__carinho:
            total += produto.preco
        return total
    @property
    def carinho(self):
        return self.__carinho

class Produto:
    def __init__(self, tipo, preco):
        self.tipo = tipo
        self.preco = preco




