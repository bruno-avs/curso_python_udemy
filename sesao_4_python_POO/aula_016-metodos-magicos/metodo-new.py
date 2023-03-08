class Magica:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)

        if not hasattr(cls, '_exist'):
            cls._exist = object.__new__(cls)

        return cls._exist

    def __init__(self, name, old):
        self.name = name
        self.old = old


magica = Magica('Bruno', 20)
magica_2 = Magica('Bruno', 50)
print(magica)
print(magica_2)
