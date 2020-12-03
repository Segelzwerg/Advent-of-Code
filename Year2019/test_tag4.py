from unittest import TestCase
import tag4


class Test(TestCase):
    def test_has_double_digits(self):
        password = 112345
        assert tag4.has_double_digits(password) == True, "112345 not found"

    def test_has_not_double_digits(self):
        password = 123456
        assert tag4.has_double_digits(password) == False, "123456 not found"

    def test_has_triple_digits(self):
        password = 111234
        assert tag4.has_double_digits(password) == False, "111234 not found"

    def test_has_quadroble_digits(self):
        password = 111134
        assert tag4.has_double_digits(password) == False, "111134 not found"

    def test_has_double_at_end_digits(self):
        password = 123455
        assert tag4.has_double_digits(password) == True, "123455 not found"

    def test_has_triple_at_end_digits(self):
        password = 123555
        assert tag4.has_double_digits(password) == False, "123555 not found"

    def test_is_all_same(self):
        password = 111111
        assert tag4.has_double_digits(password) == False, "111111 not found"

    def test_is_all_same_but_last(self):
        password = 111112
        assert tag4.has_double_digits(password) == False, "111112 not found"

    def test_is_all_same_but_first(self):
        password = 211111
        assert tag4.has_double_digits(password) == False, "211111 not found"

    def test_triple_in_middle(self):
        password = 122234
        assert tag4.has_double_digits(password) == False, "122234 not found"

    def test_quintuple_at_end(self):
        password = 122222
        assert tag4.has_double_digits(password) == False, "122222 not found"

    def test_quadrotuple_in_middle(self):
        password = 122224
        assert tag4.has_double_digits(password) == False, "122224 not found"

    def test_quadrotuple_at_beginning_but_double_at_end(self):
        password = 111122
        assert tag4.has_double_digits(password) == True, "111122 not found"

    def test_quadrotuple_in_middle_but_decremental(self):
        password = 122220
        assert tag4.has_double_digits(password) == False, "122220 not found"
        assert tag4.is_incremental(password) == False, "122220 not found"

    def test_is_incremental(self):
        password = 112345
        assert tag4.is_incremental(password) == True, "112345 not found"

    def test_is_not_incremental(self):
        password = 123450
        assert tag4.is_incremental(password) == False, "123450 not found"
