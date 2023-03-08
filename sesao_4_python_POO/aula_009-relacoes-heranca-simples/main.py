from classes import Pessoa, Estudante, Cliente

pessoa = Pessoa('Bruno', 'alves', 20)
pessoa.falar()

print()
print('#' * 50)
print()

estudante = Estudante('Bruno', 'alves', 20)
estudante.falar()
estudante.estudar()
estudante.parar_estudar()

print()
print('#' * 50)
print()

cliente = Cliente('Bruno', 'alves', 20)
cliente.falar()
cliente.comprar()
cliente.parar_comprar()

