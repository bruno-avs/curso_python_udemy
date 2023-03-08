import requests
import json


class DataBase:
    def __init__(self) -> None:
        self.url_svr = "https://testes-data-default-rtdb.firebaseio.com/"
        self.operation_url = self.url_svr + ".json"

        self.ids_on_server = requests.get()

    def get_id_data(self, id):
        url_to_id = self.url_svr + id + ".json"
        response = requests.get(url_to_id)

        if response.status_code == 200:
            return response.json()

    def get(self):
        response = requests.get(self.operation_url)

        if response.status_code == 200:
            return response.json()

    def get_ids(self):
        data: dict = self.get()

        if data is None:
            return

        ids: list = []
        for id in data.keys():
            ids.append(id)

        return ids

    def post(self, data):
        dt_js = json.dumps(data)
        response = requests.post(self.operation_url, dt_js)
        return response.status_code

    def put(self, data):
        len_ids = len(self.get_ids())
        url_to_id = self.url_svr + str(len_ids) + ".json"

        dt_js = json.dumps(data)
        response = requests.put(url_to_id, dt_js)
        return response.status_code

    def delete_all(self):
        response = requests.delete(self.url_svr)
        return response.status_code

    def delete_id(self, id):
        pass


data_base = DataBase()
data = {"name": "Dany", "last name": "Alves", "old": 4}
print(data_base.put(data))
ids = data_base.get_ids()

print(data_base.get_id_data(ids[0]))
