from itertools import product
"""
https://www.geeksforgeeks.org/python-itertools-product/
https://www.hackerrank.com/challenges/itertools-product/problem
"""
# Product retorna o produto cartesiano de dois ou mais iteráveis 
cord_1 = (1, 2, 3)
cord_2 = (8, 9)

produto = product(cord_1, cord_2)

print(list(produto))
