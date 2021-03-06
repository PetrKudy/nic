# Generated by Django 2.2.6 on 2019-10-18 23:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgdn', models.CharField(max_length=255)),
                ('crdate', models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 19, 1, 3, 19, 316358))),
                ('erdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'domain',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DomainFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(choices=[('EXPIRED', 'EXPIRED'), ('OUTZONE', 'OUTZONE'), ('DELETE_CANDIDATE', 'DELETE_CANDIDATE')], max_length=255)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nic.Domain')),
            ],
            options={
                'db_table': 'domain_flag',
                'managed': True,
            },
        ),
    ]
