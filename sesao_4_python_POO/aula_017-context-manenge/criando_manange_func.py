from contextlib import contextmanager


def log(log_txt):
    with open("log.log", 'a') as file:
        file.write(log_txt)


@contextmanager
def context_manange(file: str, mode: str) -> iter:
    try:
        file = open(file, mode)
        yield file
    finally:
        print('Arquivo fechado.')
        log(f'Arquivo: {file}\n')

        file.close()


with context_manange('func.txt', 'wr') as file:
    file.write('Linha 01')
