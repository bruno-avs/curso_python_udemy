"""
você pode usar uma variavel que acumule valores dentro de uma while

Em python é possivel usar o else junto a while,
o else só sera executado quando a expreção no while for False
"""
counter = 0
accumulator = 0

while counter <= 5:
    print(counter, accumulator)

    if accumulator == 10:
        break

    accumulator = accumulator + counter
    counter += 1
else:
    print('A expresão do while resultou em False')
