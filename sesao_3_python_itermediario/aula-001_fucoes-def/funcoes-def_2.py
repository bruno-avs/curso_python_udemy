# È possível passar uma função como referencia a uma variável
def chamar(var):
    print(var)


def retorne(arg1, arg2):
    return arg1, arg2


var = chamar
print(retorne('ola', 'ksj'))
var('ola')
