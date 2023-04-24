import json

# as funções a seguir permitem serrilhar e deserrilhar dados

my_data = {"name": "bruno", "last_name": "alves", "old": 21}

json_dumped = json.dumps(obj=my_data, indent=2)
# converte de python para json
print(json_dumped)
print()

json_loaded = json.loads(json_dumped)
# converte de json para python
print(json_loaded)

