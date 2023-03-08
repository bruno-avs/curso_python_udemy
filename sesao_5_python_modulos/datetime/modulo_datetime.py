import datetime
"""O módulo datetime fornece classe para a manipulação de datas e horas de
maneira simples e complexa."""

min_year = datetime.MINYEAR
max_year = datetime.MAXYEAR
print(f"Menor ano possível --> {min_year}")
print(f"Maior ano possível --> {max_year}")
print("-" * 40)

year = 2002
moth = 9
day = 3

date = datetime.date(year, moth, day)
# retorna um objeto date com o ano, mês e dia no formato americano

print(
    f"datetime.date({year}, {moth}, {day})"
    f"\n --> {date}")
print("-" * 40)

hors = 20
minutes = 10
seconds = 45
milliseconds = 100

time = datetime.time(hors, minutes, seconds, milliseconds)
# retorna um objeto time com o tempo idealizado, esta classe não leva em conta
# os segundos bissextos
print(
    f"datetime.time({hors}, {minutes}, {seconds}, {milliseconds})"
    f"\n --> {time}")
print("-" * 40)

date_time = datetime.datetime(
    year, moth, day, hors, minutes, seconds, milliseconds)

print(
    f"datetime.datetime("
    f"\n{year}, {moth}, {day}, {hors}, {minutes}, {seconds}, {milliseconds})"
    f"{datetime}")

day = 10
seconds = 35
microseconds = 102
milliseconds = 233
minutes = 22
hors = 12
weeks = 1

timedelta = datetime.timedelta(
    weeks=weeks, days=day, hours=hors,
    minutes=22, microseconds=microseconds,
    milliseconds=milliseconds,
    seconds=seconds)
# a classe timedelta retorna um objeto que representa um intervalo de tempo
# este objeto pode ser usado para cálculos
print(timedelta)
