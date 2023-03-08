"""Referencia: https://www.w3schools.com/python/ref_func_print.asp"""

"""A função print é usada para imprimir dados na tela"""
speak = "Hello!! my name is Bruno"
print(speak)

"""O parâmetro sep define oq ira separar cada argumento passado a print"""
welcome_msg = "welcome Bruno!!!!"
print(speak, welcome_msg, sep=" ---- ")

"""
O parâmetro end define oque vira ao final de cada argumento passado a print
"""
print(speak, welcome_msg, end=" #######")
