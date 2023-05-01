from bs4 import BeautifulSoup
import requests

# Beautiful Soup é uma biblioteca Python de extração de dados de arquivos HTML
# e XML. Ela funciona com o seu interpretador (parser) favorito a fim de prover
# maneiras mais intuitivas de navegar, buscar e modificar uma árvore de análise
# (parse tree). Ela geralmente economiza horas ou dias de trabalho de
# programadores ao redor do mundo.
# doc => https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/

url = "https://github.com/bruno-avs"
response = requests.get(url)

if not response.ok:
    print("ERRO!!!!")

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)  # pegar tags pelo nome da tag
print(soup.title.name)  # pegar o nome da tag em si
print(soup.title.string)  # pegar o conteúdo da tag em string
# print(soup.title.parent)  # pegando o parent da tag

print()
# pegando mais de um uma tag
for tags_a in soup.find_all("a"):
    # pegando todos os links
    print(tags_a["href"])
