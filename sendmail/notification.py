from typing import List, Any

from django.core.mail import send_mail


DEFAULT_FROM_EMAIL = 'noreply@email.com'


def envia_email(subject, message, sender, receiver):
    """ envia o email com as mensagens """
    send_mail(subject, message, sender, [receiver, ])
