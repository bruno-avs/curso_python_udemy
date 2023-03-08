try:
    file = open('arqui.txt', 'w+')
    file.write('ola meu nome é bruno')
    file.seek(0)
    read = file.read()
    print(read)
finally:
    file.close()