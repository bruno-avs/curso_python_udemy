from bs4 import BeautifulSoup
import requests
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
url = "https://www.muambator.com.br/login/?next=/pacotes/pendentes/"
response = requests.get(url)

html = BeautifulSoup(response.text, "html.parser")
print(html.h1)