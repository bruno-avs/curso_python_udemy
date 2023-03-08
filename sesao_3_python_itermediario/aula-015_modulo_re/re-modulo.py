import re

string = 'Ola meu nome é bruno'

ocorrencia = re.findall('o', string)
print(ocorrencia)
print()

ocorrencia_2 = re.search('nome', string)

print(ocorrencia_2.start(), '# index inicial')
print(ocorrencia_2.end(), '# index final')
print(ocorrencia_2.span(), '# tupla contendo index inicial e final')
print(ocorrencia_2.string, '# etorna a string passada para função de pesquisa')
print(ocorrencia_2.group(), '# retorna a ocorrencia')

ocorrencia_3 = re.split(r'\s', string)
ocorrencia_4 = re.sub
print()
print(ocorrencia_3)


string_2 = 'ola meu nome é joyse'
comp = re.compile(r'\s')
ocorre = comp.findall(string_2)
print(ocorre)

cnpj = '12.342.133/0001-21'
comp_2 = re.compile(r'\D')
num = comp_2.findall(cnpj)
print()
print(num)

