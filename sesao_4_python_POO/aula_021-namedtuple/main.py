"""
Um namedtuple é uma tupla imutável que possui nomes para os seus campos
existem 2 formas de se criar uma
"""

"""
1 - forma
    A primeira forma e mais verbosa, não possibilitando uma tipagem
"""
# from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"], rename=False, defaults=[0, 0])


"""
2 - forma
    - A segunda forma é mais simples de se ler possibilitando o uso de tipagem
    - As duas formas posem ser usadas, os métodos das namedtuple continuarão
    funcionando em qualquer das formas
"""
from typing import NamedTuple


class Point(NamedTuple):
    x: int = 0
    y: int = 0


point_1 = Point(11, 20)

# usando o método _make(iterable)
print("namedtuple._make()")
# usando uma lista
a_list = [90, 22]
a_list_point = Point._make(a_list)
print("\ta_list_point ->", a_list_point)
print()

# usando uma tupla
a_tuple = (20, 11)
a_tuple_point = Point._make(a_tuple)
print("\ta_tuple_point ->", a_tuple_point)
print()

# usando um dict
a_dict = {"x": 1, "y": 2}
a_dict_point = Point._make(a_dict.values())
print("\ta_dict_point ->", a_dict_point)
print()

# convertendo uma instância em um dict
print("namedtuple._asdict()")
point_dict = Point(10, 89)
print(f"\t{point_dict._asdict()}")
print()

# trocando valores com o _replace
print("namedtuple._replace()")

original_point = Point(44, 44)
print("\toriginal_point ->", original_point)

point_replaced = original_point._replace(x=9)
print("\tpoint_replaced ->", point_replaced)
print()

# usando fields
print("namedtuple.fields")

point_fields = Point(643, 382)
print("\tpoint =", point_fields)

fields = point_fields._fields
print("\tfields = point_fields._fields")
print(f"\tfields -> {fields}")
print()

# usando fields_defaults
print("namedtuple.field_defaults")

point_field_defaults = Point(3919, 2134)
print("\tpoint =", point_field_defaults)

field_defaults = point_field_defaults._field_defaults
print("\tfield_defaults = point_field_defaults._field_defaults")
print(f"\tfield_defaults {field_defaults}")
print()
