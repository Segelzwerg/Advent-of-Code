import unittest

from Year2020.Day4.passport import get_passports, count_valids


class Passport(unittest.TestCase):
    def setUp(self) -> None:
        with open('test_input.txt') as file:
            input_test = file.read().split('\n\n')
        self.passports = get_passports(input_test)
        with open('test_invalids.txt') as file:
            input_invalids = file.read().split('\n\n')
        self.invalids = get_passports(input_invalids)
        with open('test_valids.txt') as file:
            input_valids = file.read().split('\n\n')
        self.valids = get_passports(input_valids)

    def test_part1(self):
        self.assertEqual(2, count_valids(self.passports))

    def test_invalids(self):
        self.assertEqual(0, count_valids(self.invalids))

    def test_valids(self):
        self.assertEqual(4, count_valids(self.valids))
