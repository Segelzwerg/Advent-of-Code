from unittest import TestCase
import tag4


class Test(TestCase):
    def test_has_double_digits(self):
        password = 112345
        assert tag4.has_double_digits(password) == True, "112345 not found"

    def test_has_not_double_digits(self):
        password = 123456
        assert tag4.has_double_digits(password) == False, "123456 not found"

    def test_is_incremental(self):
        password = 112345
        assert tag4.is_incremental(password) == True, "112345 not found"

    def test_is_not_incremental(self):
        password = 123450
        assert tag4.is_incremental(password) == False, "123450 not found"
