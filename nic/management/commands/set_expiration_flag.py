from django.core.management.base import BaseCommand
from nic.models import DomainFlag
from datetime import datetime


class Command(BaseCommand):
    help = 'Making Cron schedule to check database and set flag to expire if outdated'

    def handle(self, *args, **options):
        domain_fl = DomainFlag.objects.filter(valid_to__date=datetime.now().date())
        for flag in domain_fl:
            flag.flag = "EXPIRED"
            flag.save()
