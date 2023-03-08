def func_1(func_2, aa):
    def func_3(*args, **kwargs):
        print(aa)
        func_2()
    return func_3

@func_1
def func_2():
    print('ola eu sou a função 2')

func_2()



# def func_4():
#     print('ola eu sou a função 4')
#
#
#
# func_4 = func_1(func_4, 'ola')
#
#
# func_4()

