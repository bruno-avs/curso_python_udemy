import calendar
import locale

# Este modulo fornece funções uteis relacionadas a calendários. por padrão,
# esses calendários tem segunda como primeiro dia da semana (0) e domingo dendo
# o ultimo dia (6). Você pode setar o primeiro dia da semana usando o método
# setfirstweekday()

my_calendar = calendar.Calendar()
# esta classe retorna um objeto calendar cujo primeiro dia da semana pode ser
# definido passando um inteiro de 0 a 6, ou usando as enumerações

weekdays = my_calendar.iterweekdays()
# retorna um iterador com os números referentes a cada dia da semana

print("calendar.iterweekdays() -> int(dia da semana)")
# for day in weekdays:
#     print(f"\t{day}")

print("-" * 79)

month_dates = my_calendar.itermonthdates(2023, 4)
# retorna um iterador em que cada valor é um objeto date que referencia um dia
# do mes informado. este método retorna todos os dias antes e depois do mes
# necessários para compor uma semana fechada, isso significa que ele não retorna
# os dias do mes fechados (30 | 31)

print("calendar.itermonthdates(2023, 4) -> date(dia do mes)")
# for date in month_dates:
#     print(f"\t{date}")

print("-" * 79)

month_days = my_calendar.itermonthdays(2023, 4)
# é semelhante ao método anterior, as diferenças são que este não retorna um
# objeto date para cada dia do mes e sim o número do mes (int).
# outra diferença é que os números que corresponderem a dias que estiverem fora
# do mes serão 0, no caso os dias que são retornados para completar a semana
# fechada

print("calendar.itermonthdays(2023, 4) -> int(dia do mes)")
# for month_day in month_days:
#     print(f"\t{month_day}")

print("-" * 79)

month_days2 = my_calendar.itermonthdays2(2023, 4)
# também é semelhante ao método anterior a diferença é que este retorna
# uma tupla com o primeiro valor sendo o dia do mes e o segundo o dia da semana
# referente a este mes (dia do mes, dia da semana)

print("calendar.itermonthdays2(2023, 4) -> tuple(dia do mes, dia da semana)")

# for month_day2 in month_days2:
#     print(f"\t{month_day2}")

print("-" * 79)

month_days3 = my_calendar.itermonthdays3(2023, 4)
# também é semelhante ao método anterior a diferença é que este retorna uma
# tupla com o primeiro valor sendo o ano, o segundo o mes e o terceiro
# o dia do mes

print("calendar.itermonthdays3(2023, 4)" "-> tuple(ano, mes, dia do mes)")

# for month_day3 in month_days3:
#     print(f"{month_day3}")

print("-" * 79)

month_days4 = my_calendar.itermonthdays4(2023, 4)
# também é semelhante ao método anterior a diferença é que este retorna uma
# tupla com o primeiro valor sendo o ano, o segundo o mes, o terceiro o dia do
# mes e o quarto o dia da semana

print(
    "calendar.itermonthdays4(2023, 4) " "-> tuple(ano, mes, dia do mes, dia da semana)"
)
# for month_day4 in month_days4:
#     print(f"{month_day4}")

print("-" * 79)

month_dates_calendar = my_calendar.monthdatescalendar(2023, 4)
# este método retorna uma lista em que cada valor é uma lista referente a uma
# semana do mes especificado, esta lista contem objetos date
print(
    "calendar.monthdatescalendar(2023, 4)"
    " -> list[ list[date]] = semanas[dates[date]]"
)
# week_count = 0

# for week in month_dates_calendar:
#     print()
#     print(f"\tsemana -> {week_count}")

#     for date in week:
#         print(f"\t{date}")
#     week_count += 1

print("-" * 79)


month_days2_calendar = my_calendar.monthdays2calendar(2023, 4)
# retorna um a lista em que cada item é um lista referente a semana, esta lista
# contem o dia do mes e o dia da semana

print(
    "calendar.monthdays2calendar(2023, 4)"
    " -> list[list[tuple(dia do mes, dia da semana)]]"
)
# week2_count = 0
# for week2 in month_days2_calendar:
#     print(f"\tsemana -> {week2_count}")
#     for day in week2:
#         print(f"\t{day}")
#     week2_count += 1


print("-" * 79)

month_days_calendar = my_calendar.monthdayscalendar(2023, 4)
# retorna uma lista em que cada item é uma lista referente as semanas do mes
# especificado, cada lista de semana contem os números do mes

print("calendar.monthdayscalendar(2023, 4) -> list[list[dia do mes]]")

# weekdays_count = 0
# for weekdays in month_days_calendar:
#     print(f"\tsemana -> {weekdays_count}")
#     for day in weekdays:
#         print(f"\t{day}")
#     weekdays_count += 1

print("-" * 79)

year_dates_calendar = my_calendar.yeardatescalendar(2023)
print("my_calendar.yeardatescalendar(2023)")
# for d in year_dates_calendar:
#     for f in d:
#         for r in f:
#             for g in r:
#                 print(g)

print("-" * 79)

text_calendar = calendar.TextCalendar()
print("calendar.TextCalendar()")
# print(text_calendar.formatmonth(2023, 4, 9, 3))
# print(text_calendar.formatyear(2023, 4))

print("-" * 79)

html_calendar = calendar.HTMLCalendar()
print("calendar.HTMLCalendar()")
# print(html_calendar.formatmonth(2023, 4))
# print(html_calendar.formatyear(2023))
# print(html_calendar.formatyearpage(2023))

print("-" * 79)
locale.setlocale(locale.LC_ALL, "pt-br.utf-8")
print(calendar.isleap(2024))
# retorna true se o ano for bissexto
print(calendar.leapdays(2023, 2033))
# retorna o número de anos bissextos entre o intervalo de anos informado
print(calendar.weekday(2023, 4, 5))
# retorna o dia da semana em relação ao dia do mês e ano especificado
print(calendar.weekheader(20))
# retorna um cabeçalho contendo os nomes dos dias da semana
print(calendar.monthrange(2023, 4))
# retorna uma tupla com o primeiro valor sendo o dia da semana do primeiro dia
# do mês especificado, o segundo valor é i número de dias no mês
print(calendar.monthcalendar(2023, 4))
# Retorna uma matriz que representa o calendário de um mês. Cada linha
# representa uma semana; os dias fora do mês são representados por zeros
print(calendar.month(2023, 4))
# Retorna o calendário de um mês em uma string de várias linhas usando o
# formatmonth() da TextCalendar classe
print(calendar.calendar(2023))
# Retorna um calendário de 3 colunas para um ano inteiro como uma string de 
# várias linhas usando o formatyear()da TextCalendar classe.
print(list(calendar.day_name))
print(list(calendar.day_abbr))
print(list(calendar.month_name))

