from pathlib import Path
from datetime import date, timedelta
import locale
import string

# A classe template recebe uma string com placeholder ($identifier), a classe
# também fornece métodos para a alteração do valor desse placeholder

PATH_TO_MESSAGE_FILE = Path(__file__).parent / "templates" / "messenger.txt"
# pego o caminho do arquivo que servira como template

current_date = date.today()
next_installment_date = current_date + timedelta(days=30)
# calculo a data do proximo pagamento

locale.setlocale(locale.LC_ALL, "")

initial_loan = locale.currency(1_000_000, grouping=True)
final_amount_with_interest = locale.currency(1_139_000, grouping=True)
# converto tudo para o para currency

mapping = {
    "name": "Bruno",
    "date": next_installment_date.strftime("%d%m%Y"),
    "initial_value": initial_loan,
    "final_value": final_amount_with_interest,
}

with open(PATH_TO_MESSAGE_FILE, "r", newline="", encoding="utf-8") as file:
    template = string.Template(file.read())  # crio o objeto template
    new_template = template.substitute(mapping)  # substituo
    print(new_template)
