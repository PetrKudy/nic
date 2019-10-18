# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime


class Domain(models.Model):
    fgdn = models.CharField(max_length=255)
    crdate = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    erdate = models.DateTimeField(blank=True, null=True)
    exdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'domain'

    def __str__(self):
        return self.fgdn


class DomainFlag(models.Model):
    flag_choices = [
            ('EXPIRED', 'EXPIRED'),
            ('OUTZONE', 'OUTZONE'),
            ('DELETE_CANDIDATE', 'DELETE_CANDIDATE'),
        ]
    domain = models.ForeignKey(Domain, models.DO_NOTHING)
    flag = models.CharField(choices=flag_choices, max_length=255)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'domain_flag'
