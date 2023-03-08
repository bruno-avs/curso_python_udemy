name = input('Please, say your name: ')
ingredients = []

is_fininsh = False
while not is_fininsh:
    input_txt = 'Please, tell us the ingredients you wanted in your sandwich: '
    ingredients.append(input(input_txt))

    fininsh = input('type (n) to end: ')
    if fininsh.lower() == 'n':
        is_fininsh = True

def inform_the_ingredients(name, *args):
    print(f'hello {name} your requested ingredients are: ')
    for ingredient in args:
        print(f'- {ingredient}')

inform_the_ingredients(name, *ingredients)