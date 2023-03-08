# https://requests.readthedocs.io/en/latest/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup
url = "https://requests.readthedocs.io/en/latest/"
response = requests.get(url)

html = BeautifulSoup(response.text, "html.parser")

body = html.select_one("#requests-http-for-humans")

print(body.select_one("h1").text)
print()
for p in body.select("p"):
    print(p.text)