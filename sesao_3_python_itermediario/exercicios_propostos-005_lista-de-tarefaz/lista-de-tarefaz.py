print('Digite o item que deseja adicionar. '
      'pra desfazer digite(d), pra refazer dígite(r), pra ver a lista completa digite(v).')


def add(task, list_of_added):
    list_of_added.append(task)
    return f'A tarefa {task} foi adicionado a lista de tarefas.'


def remove(list_of_added, list_of_removed):
    task = list_of_added.pop()
    list_of_removed.append(task)
    return f'A tarefa {task} foi removido da lista de tarefas.'


def refactory(list_of_added, list_of_removed):
    task = list_of_removed.pop()
    list_of_added.append(task)
    return f'A tarefa {task} foi adicionada novamente a lista de tarefas.'


list_of_added = []
list_of_removed = []
msg = ''
while True:
    task = input(': ')
    if len(task) != 0:
        if task.lower() == 'd' and len(list_of_added) != 0:
            msg = remove(list_of_added, list_of_removed)

        elif task.lower() == 'r' and len(list_of_removed) != 0:
            msg = refactory(list_of_added, list_of_removed)

        elif task.lower() == 'v' and len(list_of_added) != 0:
            for item in list_of_added:
                print(item + ', ', end='')
            msg = ''

        else:
            msg = add(task, list_of_added)
        print(msg)
    else:
        print('Por favor digite algo.')