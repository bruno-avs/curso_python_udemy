import random

# O método seed() é utilizado para definir o número inicial inteiro que servira
# como base para geração de números flutuantes aleatórios

# se não for informado nenhum valor, o número utilizado como semente sera o
# horário atual do sistema

random.seed(3)
print(random.random())
print(random.random())

print()

random.seed(2)
print(random.random())
print(random.random())

print()

random.seed()
print(random.random())
print(random.random())
