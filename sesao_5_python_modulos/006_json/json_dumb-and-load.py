import json


my_data = {"name": "bruno", "last_name": "alves", "old": 21}
JSON_FILE_NAME = "test_file.json"

with open(JSON_FILE_NAME, "w", encoding="utf-8") as fl:
    json.dump(my_data, fl, indent=2)


with open(JSON_FILE_NAME, "r", encoding="utf-8") as fl:
    data = json.load(fl)
    print(data)
