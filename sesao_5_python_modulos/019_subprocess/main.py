import subprocess

# O módulo subprocess permite gerar novos processos conectando-se aos seus
# canais de entrada/saída/erro obtendo o código de retorno.
# doc oficial: https://docs.python.org/pt-br/3/library/subprocess.html
# DigitalOcean: https://www.digitalocean.com/community/tutorials/how-to-use-subprocess-to-run-external-programs-in-python-3


# args é o comando a ser passado pra ser executado pelo process, se shell for
# True ele deve ser uma string, caso contrario uma lista.
args = ["ping", "127.0.0.1"]

# input é entrada que sera enviada a stdin, deve ser em bytes se text, encoding
# ou erros não forem especificados, caso contrario pode ser uma string
p_input = "entrada enviada"

# capture_output se for True, captura o retorno que o processo gerara, no caso
# stdout e stderr
capture_output = True

# se for True executa o comando utilizando o shell
shell = False

# se for True, a saída e entrada processo serão em texto, sendo decodificadas
# automaticamente usando a codificação padrão do sistema
text = True

# encoding permite definir a codificação que sera usada para codificar a
# entrada e decodificar a saída.
encoding = "cp852"

# timeout permite definir um tempo limite para execução do processo, se o
# processo demorar mais do que o tempo limite um erro sera levantado
timeout = 8

# check for True, todo o código de retorno da saída que for diferente de 0
# levantara um erro
check = True


result = subprocess.run(
    args=args,
    capture_output=True,
    text=text,
    encoding=encoding,
    timeout=timeout,
    check=check,
    shell=shell,
)

print("args =>", result.args)
print("return code =>", result.returncode)
print()
print("output =>", result.stdout)
print()
print("errors =>", result.stderr)
print()
