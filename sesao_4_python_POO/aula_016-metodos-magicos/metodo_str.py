class StrClass:
    def __init__(self):
        pass

    def __str__(self):
        return f'class => {__class__.__name__}'


strClass = StrClass()

print(strClass)
