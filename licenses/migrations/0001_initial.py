# Generated by Django 3.1 on 2020-08-30 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import licenses.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=120, unique=True)),
                ('poc_contact_name', models.CharField(max_length=120)),
                ('poc_contact_email', models.EmailField(max_length=254)),
                ('admin_poc', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.PositiveIntegerField(choices=[(0, 'javascript_sdk'), (1, 'ios_sdk'), (2, 'android_sdk')])),
                ('license_type', models.PositiveIntegerField(choices=[(0, 'production'), (1, 'evaluation')])),
                ('expiration_datetime', models.DateTimeField(default=licenses.models.get_default_license_expiration)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licenses.client')),
            ],
        ),
    ]
