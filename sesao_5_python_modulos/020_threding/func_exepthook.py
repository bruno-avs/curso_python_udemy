# a exepthook permite lidas com exceções  inesperadas, não capturadas, geradas
# por threading.run()

# a função exepthook pode ser substituída por um outra função, permitindo que
# possamos criar nossos próprios ganchos de exceção
from threading import Thread, ExceptHookArgs
import threading


def except_hook(args: ExceptHookArgs):
    print("ERROR")
    print(args.thread)
    print(args.exc_type)
    print(args.exc_value)
    print(args.exc_traceback)


def odd_or_even(number: int):
    if number % 2 == 0:
        print("par")
        return
    d = 0 / 0
    print(d)
    print("impar")


T1 = Thread(target=odd_or_even, args=(4,))
T2 = Thread(target=odd_or_even, args=(3,))

threading.excepthook = except_hook

T1.start()
T2.start()
