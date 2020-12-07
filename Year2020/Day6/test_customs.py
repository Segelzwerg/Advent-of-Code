from unittest import TestCase

from Year2020.Day6.customs import unique_answers


class CustomsTestCase(TestCase):
    def test_unique_count(self):
        answers = ['aaa', 'bca', 'bccd']
        self.assertEqual(4, unique_answers(answers))
