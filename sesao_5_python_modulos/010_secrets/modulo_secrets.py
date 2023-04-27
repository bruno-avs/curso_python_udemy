import secrets

# O módulo secrets é usado para gerar números aleatórios criptograficamente
# fortes, adequados para o gerenciamento de dados, como senhas, autenticação de
# conta, tokens de segurança e segredos relacionados.

random = secrets.SystemRandom()
# a instancia dessa classe possui os mesmos métodos de random modulo

print(secrets.randbelow(9))
# retorna um número aleatório entre 0 e o número especificado
print()

print(secrets.randbits(23))
# Retorna um int com 23 bits aleatórios
print()

# O módulo secrets também fornece funções para gerar tokens