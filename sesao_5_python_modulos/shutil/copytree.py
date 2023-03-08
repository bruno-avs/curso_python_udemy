import os
import shutil
# este método permite copiar recursivamente um caminho,
# criando a cópia do zero em outro lugar

src_path = os.path.abspath('.')
dest_path = os.path.abspath("new")


shutil.copytree(src_path, dest_path)
