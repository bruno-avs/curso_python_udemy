class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco
        self.__endereco = None

    def add_endereco(self, estado, cidade, CEP):
        self.__endereco = Endereco(estado, cidade, CEP)

    def list_dados(self):
        print(self.produto, self.preco)

        if self.__endereco:
            print(self.__endereco.estado)
            print(self.__endereco.cidade)
            print(self.__endereco.CEP)

    @property
    def endereco(self):
        return self.__endereco


class Endereco:
    def __init__(self, estado, cidade, CEP):
        self.estado = estado
        self.cidade = cidade
        self.CEP = CEP
