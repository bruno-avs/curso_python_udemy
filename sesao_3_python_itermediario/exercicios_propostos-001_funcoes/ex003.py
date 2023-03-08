# retorna o valor mais a porcentagem definida no segundo argumeto

def percentagevalue(value=10, percentage=10):
    return value + (value * percentage / 100)

value = percentagevalue(100, 10)
print(value)
