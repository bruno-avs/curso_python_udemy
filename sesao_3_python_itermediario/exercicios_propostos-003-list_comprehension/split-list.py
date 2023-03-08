sequense = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
new_lits = [''.join(v + '.' if v == '9' else v for v in sequense)]
print(new_lits)

# outro modo de solução
count = 10
new_list_2 = [sequense[n:n + count] for n in range(0, len(sequense), count)]
print(new_list_2)
formated_list = '.'.join(new_list_2)
print(formated_list)