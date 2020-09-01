
from .models import Client, License
from django.utils import timezone
from datetime import timedelta, date
from sendmail.notification import envia_email
import datetime

email_para_enviar = {}


def add_email_para_enviar(email, message, nome_cliente):
    """ monta o dict com as mensagens para enviar """
    if(nome_cliente not in email_para_enviar):
        email_para_enviar[nome_cliente] = {}
        email_para_enviar[nome_cliente]['email'] = email
        email_para_enviar[nome_cliente]['mensagens'] = []
    email_para_enviar[nome_cliente]['mensagens'].append(message)


def envia_mensagens():
    ''' envia o e-mail de alerta de licença próxima da expiração '''
    for nome_cliente in email_para_enviar:
        message_text = ''
        for mensagem in email_para_enviar[nome_cliente]['mensagens']:
            message_text += mensagem + '\n'
        envia_email('licença expirando {}'.format(nome_cliente), message_text,
                    'jpodlasnisky2@gmail.com', email_para_enviar[nome_cliente]['email'])


def trigger():
    ''' realiza as validações de data e monta as mensagens de alerta '''
    email_para_enviar.clear()
    EXPIRATION_DATE_4_MONTH = timezone.now() + timedelta(days=120)
    EXPIRATION_DATE_1_MONTH = timezone.now() + timedelta(days=30)
    EXPIRATION_DATE_1_WEEK = timezone.now() + timedelta(days=7)
    WEEK_DAY = datetime.datetime.today().weekday()
    license_list = License.objects.order_by('-expiration_datetime').all()

    for license_temp in license_list:
        if license_temp.package == 0:
            license_temp.package = 'javascript_sdk'
        elif license_temp.package == 1:
            license_temp.package = 'ios_sdk'
        elif license_temp.package == 2:
            license_temp.package = 'android_sdk'

        if license_temp.license_type == 0:
            license_temp.license_type = 'production'
        elif license_temp.license_type == 1:
            license_temp.license_type = 'evaluation'

        if(license_temp.expiration_datetime == EXPIRATION_DATE_4_MONTH):
            add_email_para_enviar(license_temp.client.admin_poc.email, "A licença {} {}, do cliente {} vai expirar em {}(expira em 4 meses). \nContate {} através do email {}".format(
                license_temp.package, license_temp.license_type, license_temp.client.client_name, license_temp.expiration_datetime, license_temp.client.poc_contact_name, license_temp.client.poc_contact_email), license_temp.client.client_name)

        if((license_temp.expiration_datetime <= EXPIRATION_DATE_1_MONTH) and WEEK_DAY == 0):
            add_email_para_enviar(license_temp.client.admin_poc.email, "A licença {} {}, do cliente {} vai expirar em {}(expira dentro de 1 mês). \nContate {} através do email {}".format(
                license_temp.package, license_temp.license_type, license_temp.client.client_name, license_temp.expiration_datetime, license_temp.client.poc_contact_name, license_temp.client.poc_contact_email), license_temp.client.client_name)

        if(license_temp.expiration_datetime <= EXPIRATION_DATE_1_WEEK):
            add_email_para_enviar(license_temp.client.admin_poc.email, "A licença {} {}, do cliente {} vai expirar em {}(expira dentro de 1 semana). \nContate {} através do email {}".format(
                license_temp.package, license_temp.license_type, license_temp.client.client_name, license_temp.expiration_datetime, license_temp.client.poc_contact_name, license_temp.client.poc_contact_email), license_temp.client.client_name)

    envia_mensagens()
