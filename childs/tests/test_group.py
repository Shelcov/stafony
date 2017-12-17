from django.test import TestCase
from ..models import Group


class TestGroup(TestCase):
    def setUp(self):
        self.group = Group(
            name='18ПИ'
        )

    def test_str(self):
        s = str(self.group)
        self.assertEqual(s, '18ПИ')
