class A:
    def falar(self):
        print('A executou..')


class B:
    def falar(self):
        print('B executou..')


class C(A):
    def falar(self):
        print('C executou..')


class D(B):
    def falar(self):
        print('D executou..')


class E(C, D):
    def falar(self):
        print('E executou..')

instancia = E()
instancia.falar()