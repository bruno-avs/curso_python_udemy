def fizzbuzz(value):
    is_divi_by_2 = value % 3 == 0
    is_divi_by_5 = value % 5 == 0

    if is_divi_by_2 and is_divi_by_5: return 'fizzBuzz'
    if is_divi_by_2: return 'fizz'
    return 'buzz' if is_divi_by_5 else value

value = fizzbuzz(11)

print(value)