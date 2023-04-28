from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from smtplib import SMTP

from datetime import date, timedelta
from string import Template
from pathlib import Path
from dotenv import load_dotenv
import locale
import json
import os

"""
Mostrarei aqui como enviar email com python utilizando o servidor SMTP.
certifique-se em ter uma conta no gmail, com uma senha de app valida
para o envio dos emails via código.

link de como fazer.
    https://support.google.com/accounts/answer/185833?hl=pt-BR

"""

ABS_PATH = Path(__file__).parent.parent

# configurando o caminho para todas as pastas

AUDIO_FD = ABS_PATH / "auds"
CONFIG_FD = ABS_PATH / "confs"
DATABASE_FD = ABS_PATH / "database"
DOCUMENT_FD = ABS_PATH / "docs"
IMAGE_FD = ABS_PATH / "imgs"
TEMPLATE_FD = ABS_PATH / "templates"

# configurando o caminho para as configurações
ENV_SMTP_FILE_PATH = CONFIG_FD / ".env.smtp"
ENV_FILE_PATH = CONFIG_FD / ".env"

# carregando as configurações do servidor
load_dotenv(ENV_SMTP_FILE_PATH)

# carregando as configurações da conta do GMAIL
load_dotenv(ENV_FILE_PATH)

# pegando as configurações
SMTP_HOST = os.getenv("SMTP_HOST") or ""
SMTP_PORT = os.getenv("SMTP_PORT") or 0

SMTP_EMAIL = os.getenv("SMTP_EMAIL") or ""
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD") or ""

# pagando as informações da empresa e do cliente
COMPANY_DATA_FILE_PATH = DATABASE_FD / "company_data.json"
CLIENT_DATA_FILE_PATH = DATABASE_FD / "user_datas.json"

company_data: dict
with open(COMPANY_DATA_FILE_PATH, "r", encoding="utf-8") as file:
    company_data = json.load(file)

client_data: dict
with open(CLIENT_DATA_FILE_PATH, "r", encoding="utf-8") as file:
    client_data = json.load(file)

# pegando o template do email e substituindo as informações
TEMPLATE_FILE_PATH = TEMPLATE_FD / "non-payment-reminder.html"

with open(TEMPLATE_FILE_PATH, "r", encoding="utf-8") as file:
    template = Template(file.read())

    today_date = date.today()
    written_date = today_date.strftime("%d do %m de %Y")
    next_invoice = today_date + timedelta(days=30)
    invoice_due_date = next_invoice.strftime("%d/%m/%Y")

    locale.setlocale(locale.LC_ALL, "")
    invoice_amount_ftm = locale.currency(client_data["invoice_amount"], grouping=True)

    replaced_template = template.substitute(
        city_name=company_data["city_name"].title(),
        company_name=company_data["name"].title(),
        written_date=written_date,
        invoice_date=invoice_due_date,
        invoice_amount=invoice_amount_ftm,
        client_name=client_data["name"].title(),
    )

# criando o objeto de EMAIL
msg = MIMEMultipart()
msg["from"] = company_data["name"]
msg["to"] = os.getenv("EMAIL_WHERE_TO_SEND")
msg["subject"] = "Email de lembrete: pagamento da fatura"

# adicionado o conteúdo ao EMAIL
body_msg = MIMEText(replaced_template, "html", "utf-8")
msg.attach(body_msg)

# adicionado imagens
IMAGE_FILE_PATH = IMAGE_FD / "flexi.png"

with open(IMAGE_FILE_PATH, "rb") as img:
    mime_img = MIMEImage(img.read(), name=os.path.basename(IMAGE_FILE_PATH))
    msg.attach(mime_img)

# adicionado audios
AUDIO_FILE_PATH = AUDIO_FD / "24K Magic - Bruno Mars (Lyrics)_160k.mp3"

with open(AUDIO_FILE_PATH, "rb") as aud:
    mime_aud = MIMEAudio(aud.read(), ".mp3", name=os.path.basename(AUDIO_FILE_PATH))
    msg.attach(mime_aud)

# adicionando outros tipos de arquivos
DOCUMENT_FILE_PATH = DOCUMENT_FD / "file.csv"

with open(DOCUMENT_FILE_PATH, "rb") as doc:
    doc_name = os.path.basename(DOCUMENT_FILE_PATH)

    mime_doc = MIMEApplication(doc.read(), name=doc_name)

    mime_doc["Content-Disposition"] = f'attachment; filename="{doc_name}"'
    msg.attach(mime_doc)

with SMTP(host=SMTP_HOST, port=int(SMTP_PORT)) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
    smtp.send_message(msg)
    print("mensagem enviada")
