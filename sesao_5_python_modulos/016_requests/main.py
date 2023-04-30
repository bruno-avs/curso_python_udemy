import requests

# requests é um biblioteca HTTP que permite realizar solicitações HTTP/1.1 com
# extrema facilidade e elegância
# doc: https://requests.readthedocs.io/en/latest/

simple_response = requests.get(url="https://api.github.com/events")
# solicitações get simples
print(simple_response.headers["date"])
# outras métodos de requisição
# requests.head()
# requests.post()
# requests.put()
# requests.delete()
# requests.options()
# requests.patch()
print()

payload = {"key1": "value1", "key2": "value2"}
response_2 = requests.get("https://httpbin.org/get", params=payload)
# passando parâmetros (query string) para uma URL
print(response_2)
# para verificar se a URL foi codificada corretamente use o seguinte atributo
print(response_2.url)

print()

payload_with_list = {"key1": "value1", "key2": ["value2", "value3"]}
response_3 = requests.get("https://httpbin.org/get", params=payload_with_list)
# passando parâmetros com lista como valores
print(response_3.url)

print()

response_in_json = requests.get("https://httpbin.org/get")
print(response_in_json.encoding)
# use encoding para mudar a codificação
# a codificação é adivinhada automaticamente pelo modulo de acordo com o
# cabeçalho da resposta
print(response_in_json.text)
# use text para pegar o conteúdo da resposta

print()

response_in_json = requests.get("https://httpbin.org/get")
print(response_in_json.content)
# use content para pegar o conteúdo da resposta em bytes

print()

response_in_json = requests.get("https://httpbin.org/get")
print(response_in_json.json())
print(response_in_json.status_code)


print()

