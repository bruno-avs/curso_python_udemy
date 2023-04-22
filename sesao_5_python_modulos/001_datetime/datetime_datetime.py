from datetime import datetime, date, time
from pytz import timezone

# a classe datetime permite lidar com data e hora ao mesmo tempo
# o formato da datas sequem o padrão ISO 8601
year = 2023
month = 4
day = 21
hour = 9
minute = 45
second = 12
my_datetime = datetime(year, month, day, hour, minute, second)
print(
    f"my_datetime = datetime("
    f"{year}, {month}, {day}, {hour}, {minute}, {second}) -> {my_datetime}"
)

# Atributos de classe
print("Atributos de classe")
print("-" * 79)
datetime_min = datetime.min
datetime_max = datetime.max
datetime_resolution = datetime.resolution

print(f"\tMenor datetime possível: datetime.min -> {datetime_min}")
print(f"\tMenor datetime possível: datetime.max -> {datetime_min}")
print(
    f"\tMenor diferença entre dois objetos datetime:"
    f"datetime.resolution -> {datetime_resolution}")

# Métodos de classe
print("-" * 79)
print("Métodos da classe")

datetime_today = datetime.today()
# retorna a data e hora atuais, é um objeto ingenuo.
print(f"\tdatetime.today() -> {datetime_today}")

print()

time_zone = timezone("America/Campo_Grande")
print("\ttime_zone = timezone('America/Campo_Grande')")
datetime_now = datetime.now(time_zone)
# o now faz o mesmo que o today, a diferença é que o now possibilita a adição
# de um objeto tzinfo oque torna ele mais preciso e versátil ja que pode
# representar a data e hora atual em qualquer fuso horário
print(f"\tdatetime.now(time_zone) -> {datetime_now}")

print()

datetime_utcnow = datetime.utcnow()
# retorna a data e hora referentes ao UTC que é basicamente um fuso horário de
# referencia para o calculo de todos os outros fusos, é o substituto do Tempo
# Médio de Greenwich, o UTC possui uma precisão maior
print(f"\tdatetime.utcnow() -> {datetime_utcnow}")

print()

datetime_fromtimestamp = datetime.fromtimestamp(1682084712.0)
# converte um timestamp em um objeto datetime, possui também a possibilidade de
# adicionar uma timezone
print(f"\tdatetime.fromtimestamp(1682084712.0) -> {datetime_fromtimestamp}")

print()

datetime_utcfromtimestamp = datetime.utcfromtimestamp(1682084712.0)
# faz o mesmo que o anterior, a única diferença é que retorna a hora com o
# acrecido de UTC
print(f"\tdatetime.utcfromtimestamp(1682084712.0) -> {datetime_utcfromtimestamp}")

print()

datetime_fromordinal = datetime.fromordinal(738631)
# converte um ordinal em um objeto datetime
print(f"\tdatetime.fromordinal(738631) -> {datetime_fromordinal}")

print()

my_date = date(2023, 5, 23)
my_time = time(18, 45, 19, 34)

date_time = datetime.combine(my_date, my_time)
# este método permite combinar um objeto date com um objeto time
print(f"\tdatetime.combine({my_date}, {my_time}) -> {date_time}")

print()

str_format = "%Y-%m-%d %H:%M:%S"
str_datetime = "2023-04-21 18:06:56"
datetime_strptime = datetime.strptime(str_datetime, str_format)
print(
    f"\tdatetime_strptime = datetime.strptime({str_datetime}, {str_format})"
    f" -> {datetime_strptime}"
)

print()

# Métodos de instancia
print("Métodos de instancia")
print("-" * 79)

datetime_obj = datetime.now(time_zone)
print("\tdatetime_obj = datetime.now(time_zone)")

date_obj = datetime_obj.date()
# este método retorna um objeto date referente ao objeto datetime
print(f"\tdatetime_obj.date() -> {date_obj}")

time_obj = datetime_obj.time()
# retorna o objeto time referente a hora do objeto datetime
print(f"\tdatetime_obj.time() -> {time_obj}")

tz_info_obj = datetime_obj.timetz()
# exatamente igual ao de cima, unica diferença é que retorna o tzinfo também
print(f"\tdatetime_obj.timetz() -> {tz_info_obj}")

datetime_replaced = datetime_obj.replace(year=2222)
# permite substituir partes do objeto datetime
print(f"\tdatetime_obj.replace(year=2222) -> {datetime_replaced}")

print(f"\tdatetime_obj.timetuple() -> {datetime_obj.timetuple()}")
print(f"\tdatetime_obj.toordinal() -> {datetime_obj.toordinal()}")
print(f"\tdatetime_obj.weekday() -> {datetime_obj.weekday()}")
print(f"\tdatetime_obj.isoweekday() -> {datetime_obj.isoweekday()}")
print(f"\tdatetime_obj.isocalendar() -> {datetime_obj.isocalendar()}")
print(f"\tdatetime_obj.isoformat() -> {datetime_obj.isoformat()}")
print(
    f"\tdatetime_obj.strftime(%Y-%m-%d %H:%M:%S) -> "
    f"{datetime_obj.strftime('%Y-%m-%d %H:%M:%S')}")