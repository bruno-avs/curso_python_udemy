ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tab_2 = [v * 2 for v in ints]
tab_3 = [v * 3 for v in ints]
tab_4 = [v * 4 for v in ints]
tab_5 = [v * 5 for v in ints]
tab_6 = [v * 6 for v in ints]
tab_7 = [v * 7 for v in ints]
tab_8 = [v for v in ints if v == 0 if v == 2]
print(tab_2)
print(tab_3)
print(tab_4)
print(tab_5)
print(tab_6)
print(tab_7)

tabuada = lambda m: [v * m for v in ints]
print(tabuada(2))
comprehension_com_ifs = [v for v in ints if v % 2 == 0]
print(comprehension_com_ifs)





