from unittest import TestCase

import numpy as np

from Year2020.Day2.password import password_valid, count_valids, password_valid2, count_valids2, \
    load_input


class PasswordTestCase(TestCase):
    def setUp(self) -> None:
        self.input = np.array([[['1-3', 'a'], 'abcde'],
                               [['1-3', 'b'], 'cdefg'],
                               [['2-9', 'c'], 'ccccccccc']])
        self.policies = self.input.T[0]
        self.password = self.input.T[1]

    def test_one_is_valid(self):
        self.assertTrue(password_valid(self.input[0][0], self.input[0][1]))

    def test_two_is_invalid(self):
        self.assertFalse(password_valid(self.input[1][0], self.input[1][1]))

    def test_three_is_valid(self):
        self.assertTrue(password_valid(self.input[2][0], self.input[2][1]))

    def test_one_is_valid2(self):
        self.assertTrue(password_valid2(self.input[0][0], self.input[0][1]))

    def test_two_is_invalid2(self):
        self.assertFalse(password_valid2(self.input[1][0], self.input[1][1]))

    def test_three_is_invalid2(self):
        self.assertFalse(password_valid2(self.input[2][0], self.input[2][1]))

    def test_counter(self):
        self.assertEqual(2, count_valids(self.policies, self.password))

    def test_counter2(self):
        self.assertEqual(1, count_valids2(self.policies, self.password))

    def test_original_input(self):
        policies, passwords = load_input()

        self.assertFalse(password_valid2(policies[17], passwords[17]))

        count = count_valids2(policies, passwords)
        self.assertTrue(count < 465, msg=f'count was {count}, but should be lower than 465')

    def test_valid(self):
        array = np.array([[['1-2', 'a'], 'ab'],
                          [['1-2', 'a'], 'aa'],
                          [['11-13', 'p'], 'pdpppppppphpm'],
                          [['6-8', 'k'], 'kkklmrkqsk']])
        self.assertTrue(password_valid2(array[0][0], array[0][1]))
        self.assertFalse(password_valid2(array[1][0], array[1][1]))
        self.assertFalse(password_valid2(array[2][0], array[2][1]))
        self.assertFalse(password_valid2(array[3][0], array[3][1]))
