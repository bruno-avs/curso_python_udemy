import requests

# fazendo uma requisição para o servidor hospedado pelo python
# é necessário que o servidor esteja rodando
url = "http://localhost:3333/"
response = requests.get(url)
print("solicitação ok =>", response.ok)
print("status code =>", response.status_code)
print()
print("cookies =>", response.cookies)
print()
print("cabeçalho =>", response.headers)
print()
# print("corpo =>", response.text)
