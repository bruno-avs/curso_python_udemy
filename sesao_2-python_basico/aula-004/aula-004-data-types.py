"""
data types
str - string
int - números inteiros
float - números reais/ ponto flutuante
bool - boolean/lógicos
"""
print("string")
print(12)
print(12.4)
print(10 == 10)

print("string", type("string"))
print(12, type(12))
print(12.4, type(12.4))
print(10 == 10, type(10 == 10))

# Convertendo dados
str()  # converte para string
int()  # para números inteiros
float()  # para números reais
bool()  # coverte para boolean

print(type(str(10)), type(int("20")), float("20"), type(bool('')) )
