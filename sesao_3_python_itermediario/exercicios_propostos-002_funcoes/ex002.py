def saldacao(name):
    return f'Ola {name}'

def fullname(name, latname):
    return name + " " + latname

def function1(name, lastname, function2, function3):
    return function2(name), function3(name, lastname)



func1, func2 = function1('bruno','alves', saldacao, fullname)
print(func1, func2, sep='\n')




# função que retorna um dicionario
def person(first_name, last_name):
    return {
        'name': first_name,
        'last_name': last_name,
        'full_name': first_name + " " + last_name
    }

print(person('bruno', 'alves'))