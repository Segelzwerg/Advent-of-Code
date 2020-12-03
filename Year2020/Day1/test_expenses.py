from unittest import TestCase

from Year2020.Day1.expenses import expenses


class ExpensesTestCase(TestCase):
    def test_with_example(self):
        input = (1721, 979, 366, 299, 675, 1456)
        self.assertEqual(514579, expenses(input))

