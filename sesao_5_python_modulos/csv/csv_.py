from typing import Sequence, Any, Optional
import csv
file_name = "user_data.csv"
# lendo o arquivo com reader
with open(file_name, newline="") as fl:
    fl_reader = csv.reader(
        fl, dialect="excel", skipinitialspace=True, strict=True)

    for row in fl_reader:
        print(row)

# lendo o arquivo com DictReader
with open(file_name, newline="") as fl:
    names: Optional[Sequence[str]] = None
    key_name: str | None = None
    value_name: str | None = "Sem valor"

    fl_dictreader: Any = csv.DictReader(
        fl,
        fieldnames=names,
        restkey=key_name,
        restval=value_name,
        skipinitialspace=True,
    )
    for row in fl_dictreader:
        print(row)

# escrevendo em arquivos
with open(file_name, newline="") as csvfile:
    csv_datas = csv.reader(csvfile, skipinitialspace=True)
    csv_datas = list(csv_datas)

with open("user_data_02.csv", "w", newline="") as csvfile:
    dialect = "excel"
    delimiter = ","
    quotechar = '"'

    csvwriter = csv.writer(
        csvfile,
        dialect=dialect,
        delimiter=delimiter,
        quotechar=quotechar,
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    )

    for row in csv_datas:
        fmt_row = [
            value.title() if value.isalpha() else value
            for value in row
        ]
        csvwriter.writerow(fmt_row)
