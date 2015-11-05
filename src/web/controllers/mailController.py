from models.mail import Mail
from bottle import request


class MailController:

    def __init__(self, p_env, p_mail_service):
        self.env = p_env
        self.mail_service = p_mail_service

    def create(self):
        name = request.params["name"]
        sender_mail = request.params["email"]
        phone = "88888888"
        msg = request.params["message"]
        mail = Mail(name, sender_mail, phone, msg)
        self.mail_service.send(mail)
