import os

lista = os.listdir() # retorna totos os nomes dor arquivos
print(lista)

# os.mkdir('nova_pasta')

lista_2 = os.listdir()
print(lista_2)

# r = os.chdir('nova_pasta')

# arqui_1 = os.path.abspath('ola.txt').replace('User ', '')
# arqui_2 = os.path.abspath('ola-2.txt.txt').replace('User ', '')
# print(arqui_1)
# print(arqui_2)
# y = os.system('zip ola.zip ola-2.txt')
#
# print(y)
p = os.getcwd()
print(p)
os.chdir(r'nova_pasta')
print(os.getcwd())

d = os.walk(p)


for root, dirs, files in d:
    print(root)

print(os.path.exists(r'D:\User\Documentos\Curso-de-python\pythonAulas\aula-012_modulo-OS\pasta'))

print(str.rfind('doc.f', '.'))