"""
O módulo locale abre o acesso ao banco de dados de localidade POSIX e
funcionalidade. O mecanismo de localidade POSIX permite que os programadores
lidem com certas questões culturais em uma aplicação, sem exigir que o
programador conheça todas as especificidades de cada país onde o software é
executado.

O módulo locale é implementado em cima do módulo _locale, que por sua vez usa
uma implementação a localidade ANSI C se disponível.
"""
import locale
import calendar

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

my_calendar = calendar.calendar(2023)

print(my_calendar)
print()
print(locale.localeconv())
