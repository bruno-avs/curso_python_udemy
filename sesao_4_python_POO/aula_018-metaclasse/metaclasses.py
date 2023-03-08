class MyMetaClass(type):
    def __new__(mcs, name, bases, namespace):
        name_metod = "printar"

        if not name_metod in namespace:
            raise NotImplementedError(
                f'O método {name_metod} precisa ser definido'
            )
        else:
            if not callable(namespace[name_metod]):
                raise NotImplementedError(
                    f'O método {name_metod} precisa ser definido'
                )

        return type.__new__(mcs, name, bases, namespace)


class ChildMeta(metaclass=MyMetaClass):
    printar = 'pspap'
