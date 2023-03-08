from data import products
print(products)

def almenta(p):
    p['value'] += p['value'] * 10 / 100
    return p

almento = map(almenta, products)

print(list(almento))