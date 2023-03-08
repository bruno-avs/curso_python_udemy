from itertools import count
"""
https://www.geeksforgeeks.org/python-itertools-count/
"""
start = 0
step = 1
ids = count(start=start, step=step)
# count é basicamente um gerador de números infinitos, ele retorna um iterador
# que cada vez que for executado retorna um número acima

names = ["bruno", "Luscas", "rodrigo", "pedro"]
zipper = zip(ids, names)
account = {}

for id, name in zipper:
    account[str(id)] = name

print(account)
