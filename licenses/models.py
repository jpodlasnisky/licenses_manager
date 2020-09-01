from django.db import models
from datetime import datetime, timedelta, date
from django.contrib.auth.models import User
from django.utils import timezone

LICENSE_EXPIRATION_DELTA = timedelta(days=90)


def get_default_license_expiration():
    return timezone.now() + LICENSE_EXPIRATION_DELTA


# Create your models here.
class Client(models.Model):
    """  A client who holds licenses to packages """
    client_name = models.CharField(max_length=120, unique=True)
    poc_contact_name = models.CharField(max_length=120)
    poc_contact_email = models.EmailField()

    admin_poc = models.ForeignKey(User, limit_choices_to={
                                  'is_staff': True}, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name


class License(models.Model):
    """ Data model for a client license allowing access to a package """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    package = models.PositiveIntegerField(
        choices=((0, 'javascript_sdk'), (1, 'ios_sdk'), (2, 'android_sdk')))
    license_type = models.PositiveIntegerField(
        choices=((0, 'production'), (1, 'evaluation')))
    expiration_datetime = models.DateTimeField(
        default=get_default_license_expiration)

    def __str__(self):
        return self.client.client_name
