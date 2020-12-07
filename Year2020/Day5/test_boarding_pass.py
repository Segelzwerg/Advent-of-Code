import unittest

from Year2020.Day5.boarding_pass import determine_row, determine_column, load_data, get_seat_id


class BoardingPassTestCase(unittest.TestCase):
    def setUp(self):
        self.data = load_data('test_input.txt')

    def test_rows(self):
        self.assertEqual(44, determine_row('FBFBBFF', 0, 127))

    def test_columns(self):
        self.assertEqual(5, determine_column('RLR', 0, 7))

    def test_ex1(self):
        self.assertEqual(70, determine_row(self.data[0][0]))
        self.assertEqual(7, determine_column(self.data[0][1]))
        self.assertEqual(567, get_seat_id(self.data[0]))

    def test_ex2(self):
        self.assertEqual(14, determine_row(self.data[1][0]))
        self.assertEqual(7, determine_column(self.data[1][1]))

    def test_ex3(self):
        self.assertEqual(102, determine_row(self.data[2][0]))
        self.assertEqual(4, determine_column(self.data[2][1]))
