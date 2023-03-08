
class Geeks:
    def __init__(self):
        self._age = 0

    def get_age(self):
        print("getter method called")
        return self._age

    def set_age(self, a):
        print("setter method called")
        self._age = a

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


mark = Geeks()
print(mark.age) ## quando eu referencio o campo age a função get é executada
print('#'*20)
mark.age = 10 ## quando eu seto um novo valor a função set é executada
print('#'*20)
print(mark.age)
print('#'*20)
mark.del_age() ## assim eu deleto o valor de age



