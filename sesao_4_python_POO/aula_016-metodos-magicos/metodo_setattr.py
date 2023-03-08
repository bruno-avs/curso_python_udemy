class SetClass:
    def __init__(self, value_init):
        self.value_init = value_init

    def __setattr__(self, key, value):
        print('performed: __setattr__')

        if not isinstance(value, (int, float, bool)):
            self.__dict__[key] = value
        else:
            return





set_class = SetClass('Bruno')

set_class.value_init = 2030
print(set_class.value_init)
