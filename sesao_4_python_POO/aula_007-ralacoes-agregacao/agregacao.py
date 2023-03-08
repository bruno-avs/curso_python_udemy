from classes import CarinhoCompras, Produto

p1 = Produto('uvas', 3.00)
p2 = Produto('molho de tomate', 5.00)
p3 = Produto('coca-cola', 10.00)


carinho = CarinhoCompras()
carinho.add_produto(p1)
carinho.add_produto(p2)
carinho.add_produto(p3)

carinho.listar_produtos()

print(carinho.total())
