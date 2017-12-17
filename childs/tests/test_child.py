from django.test import TestCase
from ..models import Group, Child
from django.utils import timezone


class TestGroup(TestCase):
    def setUp(self):
        self.group = Group(
            name='18ПИ'
        )
        self.child = Child(
            name='Тестов Тест',
            birthdate=timezone.now().date(),
            group=self.group,
        )

    def test_str(self):
        s = str(self.child)
        self.assertEqual(s, 'Тестов Тест')
