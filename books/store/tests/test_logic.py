from unittest import TestCase

from store.logic import operators


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operators(6, 13, '+')
        self.assertEqual(19, result)

    def test_mines(self):
        result = operators(6, 13, '-')
        self.assertEqual(-7, result)

    def test_multiply(self):
        result = operators(6, 13, '*')
        self.assertEqual(78, result)
