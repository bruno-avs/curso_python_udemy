# A function that returns the length of the value:
def myFunc(e):
  print(e)
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)

calcular_porcentagem = lambda v, p: v * p / 100


print(calcular_porcentagem(121,10))

dic = {'nome': 'bruno'}
lis = ['ola', 'olas']
dic.update({'oal': 'osdos', 'ola': 'ola'})

print(dic.values())
