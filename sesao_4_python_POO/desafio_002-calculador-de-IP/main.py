from ip_calculator_class import IPCalculator
import re

config = IPCalculator()
d = config.calculate_ip("10.20.12.45", prefix="26")
regex_check = re.compile(r"")
is_ip = regex_check.search("101232212.20.12.45")
print(is_ip)
print(d.last_ip)

print(int("11111111", 2))