import re

texto1 = '''
Sites diversos:
https://google.com/
https://www.gov.br/
https://www.kaiamba.com.br/
http://www.faetec.rj.gov.br/
'''


domains = re.finditer(r'https?://(www\.)?([a-zA-Z0-9]+\.)+(com|br)/', texto1)
for domain in domains:
    print(domain)

emails = '''
Vários e-mails:
daniel@dominio.com
daniel.candiotto@dominio.com.br
DANIEL@dominio.br
DANIEL.CANDIOTTO@gov.br
danielcandiotto1@dominio1.co
daniel_candiotto_1@dominio-dominio.net
'''
emails_cole = re.finditer('(daniel|DANIEL)(@|.[a-zA-Z0-9]+)+', emails)
for email in emails_cole:
    print(email)

strs = 'foo foo.!@$%¨&*()_+1324335637890ç (foo) f1oobar'

d = re.findall(r'\w',strs)
print(d)