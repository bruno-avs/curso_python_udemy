from random import randint
import re


class Cartao:
    def __init__(self, name, last_name, agg, numb_conta, limite, function) -> None:
        self.name = name
        self.last_name = last_name
        self.agg = agg
        self.numb_conta = numb_conta
        self.function = function
        self.limite = limite
        self.is_block = False
        self.numb_card = None
        self.date_valid = None
        self.cod_CV = None

    @staticmethod
    def gener_numb_card():
        numb_card = str(randint(1000000000000000, 9999999999999999))
        return ' '.join(re.findall('[0-9]{4}', numb_card))

    @staticmethod
    def gener_date_valid():
        numb_valid = str(randint(1000, 9999))
        return '/'.join(re.findall('[0-9]{2}', numb_valid))

    @staticmethod
    def gener_cod_CV():
        numb_CV = str(randint(100, 1000))
        return numb_CV

    def generate_card(self):
        self.numb_card = self.gener_numb_card()
        self.date_valid = self.gener_date_valid()
        self.cod_CV = self.gener_cod_CV()
