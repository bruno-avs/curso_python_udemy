# gerenciando arquivos de forma simples
file = open('abc.txt', 'w+')
file.write('ola mundo !!!\n')
file.write('ola mundo !!!\n')
file.write('ola mundo !!!\n')
file.write('ola mundo !!!\n')
d = file.seek(0, 1)
print(d)
print(file.read())
file.seek(0)
lines = file.readlines()
print(lines)
file.close()

