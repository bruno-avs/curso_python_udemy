import requests
from datetime import date
import locale

url = "http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

response = requests.get(url)
currencys_data: dict = response.json()

for currency in currencys_data.values():
    locale.setlocale(locale.LC_ALL, "pt_br.utf-8")
    print()
    date_att = date.fromtimestamp(float(currency["timestamp"]))
    current = locale.currency(float(currency["bid"]))
    high = locale.currency(float(currency["high"]))
    low = locale.currency(float(currency["low"]))

    print(f'{currency["name"]} - {date_att.strftime("%d/%m/%y")}')
    print(f'\tCotação atual: {current}')
    print(f'\tMaior: {high}')
    print(f'\tMenor: {low}')
