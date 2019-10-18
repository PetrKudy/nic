from django.test import TestCase
from nic.models import Domain, DomainFlag
from nic.management.commands.set_expiration_flag import Command
from freezegun import freeze_time
import datetime


class ViewTest(TestCase):
    def setUp(self):
        dm1 = Domain.objects.create(
            pk=1,
            fgdn='test.cz',
            crdate='2006-10-25 14:30:59',
            erdate=None,
        )
        dm2 = Domain.objects.create(
            pk=2,
            fgdn='test.com',
            crdate='2010-10-25 14:30:59',
            erdate='2011-10-25 14:30:59',
        )
        DomainFlag.objects.create(
            domain=dm1,
            flag='EXPIRED',
            valid_from='2006-10-25 14:30:59',
            valid_to='2006-12-25 14:30:59',
        )
        DomainFlag.objects.create(
            domain=dm1,
            flag='OUTZONE',
            valid_from='2006-12-25 14:30:59',
            valid_to='2006-12-30 14:30:59',
        )
        DomainFlag.objects.create(
            domain=dm2,
            flag='DELETE_CANDIDATE',
            valid_from='2010-10-25 14:30:59',
            valid_to='2011-10-25 14:30:59',
        )

    def test_IndexView(self):
        """ Testing Index View"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['data'].count(), 1)
        self.assertContains(response, 'test.cz')
        self.assertContains(response, '<p>OUTZONE</p>')
        self.assertContains(response, "<a href=1>test.cz</a>\n")

    def test_DetailView(self):
        """ Testing Detail View"""
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>test.cz</h1>')
        self.assertContains(response, '<p>Created: Oct. 25, 2006, 2:30 p.m.</p>')
        self.assertContains(response, '<p>Disabled: None</p>')
        self.assertContains(response, '<p>OUTZONE</p>')


class CommandsTest(TestCase):
    def setUp(self):
        dm1 = Domain.objects.create(
            pk=1,
            fgdn='test.cz',
            crdate='2006-10-25 14:30:59',
            erdate=None,
        )

        DomainFlag.objects.create(
            pk=1,
            domain=dm1,
            flag='OUTZONE',
            valid_from='2006-12-25 14:30:59',
            valid_to='2006-12-30 14:30:59',
        )

    def test_command_set_expiration_flag(self):
        """ Testing command for cron"""
        with freeze_time("2006-12-30"):
            assert datetime.datetime.now() == datetime.datetime(2006, 12, 30)
            Command.handle(self)
        flag = DomainFlag.objects.get(pk=1)
        self.assertEqual(flag.flag, "EXPIRED")
