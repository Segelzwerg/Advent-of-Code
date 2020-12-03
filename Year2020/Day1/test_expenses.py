from unittest import TestCase

from Year2020.Day1.expenses import expenses, three_sum


class ExpensesTestCase(TestCase):
    def setUp(self) -> None:
        self.input_array = (1721, 979, 366, 299, 675, 1456)

    def test_with_example(self):
        self.assertEqual(514579, expenses(self.input_array))

    def test_three_sum(self):
        self.assertEqual(241861950, three_sum(self.input_array))
