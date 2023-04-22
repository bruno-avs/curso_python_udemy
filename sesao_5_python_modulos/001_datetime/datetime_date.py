from datetime import date

# classe date
# A classe date permite a criação de objetos de datas
my_date = date(year=2023, month=4, day=20)
print("date(year=2023, month=4, day=20) ->", my_date)
print()
# Atributos de class
print("-" * 79)
print("Atributos de class")
min_date = date.min
# a data representável mais antiga

print("\tdate.min ->", min_date)
max_date = date.max
# A ultima data representável
print("\tdate.max ->", max_date)
resolution_date = date.resolution
# a menor diferença possível que possa ter entre 2 objetos date
print("\tdate.resolution ->", resolution_date)
print()

# Métodos de classe
print("-" * 79)
print("Métodos de classe")
print("\ttoday")
today = date.today()  # retorna um objeto date com a data atual do sistema
print("\tdate.today() ->", today)
print()

print("\tfromtimestamp")
converted_timestamp = date.fromtimestamp(1682069940)
# converte um timestamp (carimbo de tempo) em um objeto date
# timestamp e basicamente a somatória de segundos desdo ano de 1970 até a
# data determinada
print("\tdate.fromtimestamp(1682069940) ->", converted_timestamp)
print()

print("\tfromordinal")
converted_ordinal = date.fromordinal(738631)
# converte um ordinal em um objeto date
# número ordinal é um indicador de ordem, primeiro, segundo, terceiro ...
print("\tdate.fromordinal(738631) ->", converted_ordinal)
print()


year = 2023
month = 4
day = 20
date_instance = date(year, month, day)

# Atributos de instancia
print("-" * 79)
print("Atributos de instancia")
print("\tinstancia = date(2023, 4, 20)")
print("\t\tinstance.year ->", date_instance.year)
print("\t\tinstance.month ->", date_instance.month)
print("\t\tinstance.day ->", date_instance.day)

# Métodos de instancia
print("-" * 79)
print("Métodos de instancia")
print("\tinstance = date(2023, 4, 20)")
new_year = 2002
new_month = 9
new_day = 25

replaced_date = date_instance.replace(year=new_year, month=new_month, day=new_day)
# O método replace retorna um novo objeto date onde os parâmetros informados
# são substituídos

print(
    f"\t\tinstance.replace(year={new_year}, month={new_month}, day={new_day})"
    f" -> {replaced_date}"
)

timetuple_date = date_instance.timetuple()
print(f"\t\tinstance.timetuple() ->\n\t\t{timetuple_date}")
# retorna um objeto struct_time, basicamente uma tupla, referente a instancia
print()

toordinal_date = date_instance.toordinal()
# retorna o ordinal referente a instancia
print("\t\tinstance.toordinal() ->", toordinal_date)

weekday_date = date_instance.weekday()
# retorna o dia da semana como um número inteiro, 0 a 6
print("\t\tinstance.weekday() ->", weekday_date)

iso_weekday_date = date_instance.isoweekday()
# retorna o dia da semana como um número inteiro seguindo o padrão iso, 1 a 7
print("\t\tinstance.isoweekday() ->", iso_weekday_date)

iso_calendar_date = date_instance.isocalendar()
# retorna uma tupla com 3 elementos, segundo o formato iso,
# (ano, numero de semanas, dia da semana)
print("\t\tinstance.isocalendar() ->", iso_calendar_date)

iso_format_date = date_instance.isoformat()
# retorna a data em formato de string segundo o padrão iso
print("\t\tdate_instance.isoformat() ->", iso_format_date)

ctime_date = date_instance.ctime()
# retorna a data em formato de string de um jeito mas harmonizado
print("\t\tinstance.ctime() ->", ctime_date)

strftime_date = date_instance.strftime("%d/%m/%Y")
# retorna uma string referente a instancia formatada de acordo com as diretivas
print("\t\tdate_instance.strftime('%d/%m/%Y') ->", strftime_date)
print()
