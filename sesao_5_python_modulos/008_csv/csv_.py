from typing import Sequence, Any, Optional
from pathlib import Path
import csv

FILE_NAME = "user_data.csv"
ABS_PATH = Path(__file__).parent
PATH_TO_FILE = ABS_PATH / FILE_NAME

# lendo o arquivo com reader
with open(PATH_TO_FILE, newline="", encoding="utf-8") as fl:
    fl_reader = csv.reader(fl, dialect="excel", skipinitialspace=True, strict=True)

    for row in fl_reader:
        print(row)

# lendo o arquivo com DictReader
with open(PATH_TO_FILE, newline="", encoding="utf-8") as fl:
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
with open(PATH_TO_FILE, newline="", encoding="utf-8") as csvfile:
    csv_datas = csv.reader(csvfile, skipinitialspace=True)
    csv_datas = list(csv_datas)

FILE_NAME_2 = "user_data_02.csv"
PATH_TO_FILE_2 = ABS_PATH / FILE_NAME_2

with open(PATH_TO_FILE_2, "w", newline="", encoding="utf-8") as csvfile:
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
        fmt_row = [value.title() if value.isalpha() else value for value in row]
        csvwriter.writerow(fmt_row)
