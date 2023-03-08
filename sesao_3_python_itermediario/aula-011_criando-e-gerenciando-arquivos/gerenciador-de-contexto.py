import json
data = {
    'name': 'bruno',
    'idade': 20,
    'sexo': 'masculino',
}
data_json = json.dumps(data, indent=True)
print(data_json)
with open('new.json', 'w+') as file:
    file.write(data_json)

