from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
import encodings
import smtplib
import os

from string import Template
from datetime import datetime
from locale import setlocale, LC_ALL


def send_emails(email: str, password: str):
    path_template = "template.html"
    setlocale(LC_ALL, "pt_br.utf-8")
    date = datetime.now().strftime("%A dia %d de %B de %Y")

    with open(path_template, "r", encoding="utf-8") as html:
        template = Template(html.read())
        body_msg = template.safe_substitute(name="Bruno", date=date)

    msg = MIMEMultipart()
    msg["subject"] = "Atenção: esse é um e-mail de teste"
    msg["from"] = email
    msg["to"] = "brunoalvesds1348@gmail.com"

    body = MIMEText(body_msg, "html")
    msg.attach(body)
    path_folder_img = os.path.abspath("imgs")
    path_to_img = os.path.join(path_folder_img, "pexels-ahmed.jpg")

    with open(path_to_img, "rb") as img_file:
        img = MIMEImage(
            img_file.read(),
            name=os.path.basename(path_to_img))
        msg.attach(img)

    path_folder_audio = os.path.abspath("audios")
    path_file_audio = os.path.join(path_folder_audio, "Ai Ai Ai Calma.mp3")

    with open(path_file_audio, "rb") as audio_file:
        audio = MIMEApplication(
            audio_file.read(),
            name=os.path.basename(path_file_audio))
        audio["Content-Disposition"] = f'attachment; ' \
            f'filename="{os.path.basename(path_file_audio)}"'
        msg.attach(audio)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.ehlo()
        server.starttls()
        server.login(user=email, password=password)
        server.send_message(msg)



send_emails(email, senha)
