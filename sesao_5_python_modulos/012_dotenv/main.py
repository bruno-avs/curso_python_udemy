"""
o que são variáveis de ambiente?
    - são basicamente variáveis que estão no sistema operacional.

    - você pode definir variáveis utilizando algum terminal com os comandos
    específicos.

    - em python usamos variáveis de ambiente para armazenar dados sensíveis
    como, senhas ou email, impedindo que esses dados fiquem no código em si
    evitando problemas de segurança.

    - https://pt.wikipedia.org/wiki/Vari%C3%A1vel_de_ambiente


O modulo dotenv permite setar e gerencias variáveis de ambiente de uma
maneira mais rápida e simples.

DOC oficial
    https://pypi.org/project/python-dotenv/
"""
from dotenv import load_dotenv, dotenv_values
from pathlib import Path
import os

ABS_PATH = Path(__file__).parent
CONFIG_FD = ABS_PATH / "configs"
PATH_TO_ENV = CONFIG_FD / ".env"

is_loaded = load_dotenv(dotenv_path=PATH_TO_ENV)
# Você pode carregar as variáveis de ambiente presentes no arquivo .env usando
# esta função. Ela seta todas as variáveis presentes la.

print(is_loaded)  # Ele retorna um boolean informando se o carregamento foi bem
# sucedido ou não

print(os.getenv("BD_PASSWORD"))  # pegando as variáveis no sistema

configs = dotenv_values(dotenv_path=PATH_TO_ENV)
# Este outro método permite pegar apenas o conteúdo que esta em um arquivo .env
# sem setar nada no sistema. Este método e útil pois com ele você pode pegar
# configurações de arquivos diferentes.
print(configs)


# sempre verifique se os arquivos .env estão no seu .gitignore para que eles
# não sejam enviados pro GitHub sem querer


# é recomendado sempre criar um arquivo .env.example para exemplificar para
# outro desenvolvedor quais configurações ele tem que passar
