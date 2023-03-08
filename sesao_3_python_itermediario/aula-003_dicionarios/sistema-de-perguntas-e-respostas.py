quests = {
    'quest 1': {
        'quest': 'Responda sobre a tabuada do 3.',
        'tabuada': {
            "3 X 0": '0',
            "3 X 1": '3',
            "3 X 2": '6',
            "3 X 3": '9',
            "3 X 4": '12',
            "3 X 5": '15',
            "3 X 6": '18',
            "3 X 7": '21',
            "3 X 8": '24',
            "3 X 9": '27',
            "3 X 10": '30',
        }
    },
    'quest 2': {
        'quest': 'Responda sobre a tabuada do 4.',
        'tabuada': {
            "4 X 0": '0',
            "4 X 1": '4',
            "4 X 2": '8',
            "4 X 3": '12',
            "4 X 4": '16',
            "4 X 5": '20',
            "4 X 6": '24',
            "4 X 7": '28',
            "4 X 8": '32',
            "4 X 9": '36',
            "4 X 10": '40',
        }
    },
}

for qk, qv in quests.items():
    print(qv['quest'])

    for qsk, qsv in qv['tabuada'].items():
        quest = input(f'\t{qsk}: ')

        if quest == qsv: print('\tcorrect')
        else: print('\twrong')
        