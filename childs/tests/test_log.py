from django.test import TestCase
from ..models import Group, Child, Log
from django.utils import timezone


class LogGroup(TestCase):
    def setUp(self):
        self.group = Group(
            name='18ПИ'
        )
        self.child = Child(
            name='Тестов Тест',
            birthdate=timezone.now().date(),
            group=self.group,
        )
        self.log = Log(
            child=self.child,
            parent='Папа Тестов',
        )
        self.time = timezone.now()
        self.log.event_time = self.time

    def test_str(self):
        s = str(self.log)
        self.assertEqual(s, 'Тестов Тест came в %s' % self.time)
