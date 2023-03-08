class Objects:
    def __init__(self, obj_init):
        self.obj_init = obj_init

    def __len__(self):
        total = 0
        for value in self.obj_init.values():
            if isinstance(value, (int, float, str)):
                total += 1
                continue
            total += len(value)
        return total


obj = {
    'name': 'Bruno',
    'List': [1, 2, 3, 4, 5, 6, 6, 6, 7],
    'numb': 90

}
objects = Objects(obj)

print(len(objects))
