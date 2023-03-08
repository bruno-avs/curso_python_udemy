from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from typing import Optional
import string
import smtplib
import os


class EmailSenderSMTP:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        self._host_server: str = "smtp.gmail.com"
        self._port: int = 587
        self._emails_multipart: list[MIMEMultipart] = []

    def add_content(
        self,
        subject: str = "",
        content: Optional[str] = None,
        path_html_file: Optional[str] = None,
        mapping: Optional[dict] = None,
        mapping_several: Optional[list | tuple] = None
    ) -> None:
        body_msg: MIMEText

        if content is not None:
            body_msg = MIMEText(content, "plain")
            self.define_content(body_msg, self.email, subject)

        elif path_html_file is not None:
            if not os.path.isfile(path_html_file):
                raise TypeError("the path to the image is invalid")

            html: str
            if mapping is not None:
                html = self.get_html(path_html_file, mapping)
                body_msg = MIMEText(html, "html")
                self.define_content(body_msg, self.email, subject)

            elif mapping_several is not None:

                for mp in mapping_several:
                    html = self.get_html(path_html_file, mp)
                    body_msg = MIMEText(html, "html")
                    self.define_content(body_msg, self.email, subject)

    def attach_img(
        self,
        path_to_img: str | None = None,
        path_img_attach_custom: Optional[list[str]] = None
    ) -> None:

        if path_to_img is None and path_img_attach_custom is None:
            raise TypeError(
                "EmailSenderSMTP.attach_img()"
                "please define at least one optional argument")

        if path_to_img is not None:
            if not os.path.isfile(path_to_img):
                raise TypeError("the path to the image is invalid")

            with open(path_to_img, "rb") as img_file:
                img = MIMEImage(
                    img_file.read(), name=os.path.basename(path_to_img))

                for email in self._emails_multipart:
                    email.attach(img)

        elif path_img_attach_custom is not None:
            valid_path: int = 0
            for key, path_img in enumerate(path_img_attach_custom):
                if not os.path.isfile(path_img):
                    key += 1
                    continue

                valid_path += 1
                with open(path_img, "rb") as img_file:
                    img = MIMEImage(
                        img_file.read(), name=os.path.basename(path_img))
                    self._emails_multipart[key].attach(img)

            if valid_path == 0:
                raise TypeError(
                    'nenhum dos caminhos de '
                    '"path_img_attach_custom" são válidos')

    def attach_other_files(
        self,
        path_to_file: str | None = None,
        path_file_attach_custom: Optional[list[str]] = None
    ):
        if path_to_file is None and path_file_attach_custom is None:
            raise TypeError(
                "EmailSenderSMTP.attach_other_files()"
                "please define at least one optional argument")

        if path_to_file is not None:
            if not os.path.isfile(path_to_file):
                raise TypeError("the path to the file is invalid")

            name_file = os.path.basename(path_to_file)
            with open(path_to_file, "rb") as file:
                fl = MIMEApplication(file.read(), name=name_file)
                fl["Content-Disposition"] = f'attachment; ' \
                    f'filename="{name_file}"'

                for email in self._emails_multipart:
                    email.attach(fl)

        elif path_file_attach_custom is not None:
            valid_path: int = 0
            for key, path_file in enumerate(path_file_attach_custom):
                if not os.path.isfile(path_file):
                    key += 1
                    continue

                valid_path += 1
                name_file = os.path.basename(path_file)
                with open(path_file, "rb") as file:
                    fl = MIMEApplication(file.read(), name=name_file)
                    fl["Content-Disposition"] = f'attachment; ' \
                        f'filename="{name_file}"'
                    self._emails_multipart[key].attach(fl)

            if valid_path == 0:
                raise TypeError(
                    'nenhum dos caminhos de '
                    '"path_file_attach_custom" são válidos')

    def attach_with_base(self, path_to_file):
        file_name = os.path.basename(path_to_file)

        with open(path_to_file, "rb") as file:
            fl = MIMEBase("application", "octet-stream")
            fl.set_payload(file.read())
            encoders.encode_base64(fl)
            fl.add_header(
                "Content-Disposition", f'attachment; filename="{file_name}"')
            self._multipart.attach(fl)

    def define_content(self, body_msg, from_whom, subject):
        msg = MIMEMultipart()
        msg["subject"] = subject
        msg["from"] = from_whom
        msg.attach(body_msg)
        self._emails_multipart.append(msg)

    @staticmethod
    def get_html(path_html_file, mapping):
        with open(path_html_file, "r") as html_file:
            template = string.Template(html_file)
            return template.safe_substitute(mapping)

    def send_message(self, for_whom):

        for key, email in for_whom:
            content = self._emails_multipart[key]
            content["to"] = email

            with smtplib.SMTP(self._host_server, self._port) as server:
                server.ehlo()
                server.starttls()
                server.login(self.email, self.password)
                server.sendmail(self.email, email, content.as_string())


email = "brunoalvesds333@gmail.com"
senha = "tnvgmptpaigdnmie"

subject = "ATENÇÃO: esse é um e-mail de teste."
path_html = os.path.abspath("template.html")
path_to_html_content = os.path.abspath("template.html")

email_sender = EmailSenderSMTP(email, senha)
email_sender.add_content(subject, path_html_file=path_html)
email_sender.attach_img()
