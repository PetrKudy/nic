# Generated by Django 2.2.6 on 2019-10-18 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='exdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='crdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 19, 1, 4, 23, 366566)),
        ),
    ]
