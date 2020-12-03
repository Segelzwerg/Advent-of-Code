import unittest

from Year2020.Day3.slope import count_trees, multiply


class MyTestCase(unittest.TestCase):
    def test_example_with_3(self):
        with open('test_input.txt') as file:
            tree_map = file.read().split('\n')
            self.assertEqual(7, count_trees(tree_map, 3))

    def test_example_with_1(self):
        with open('test_input.txt') as file:
            tree_map = file.read().split('\n')
            self.assertEqual(2, count_trees(tree_map, 1))

    def test_example_with_5(self):
        with open('test_input.txt') as file:
            tree_map = file.read().split('\n')
            self.assertEqual(3, count_trees(tree_map, 5))

    def test_example_with_7(self):
        with open('test_input.txt') as file:
            tree_map = file.read().split('\n')
            self.assertEqual(4, count_trees(tree_map, 7))

    def test_example_with_1_2(self):
        with open('test_input.txt') as file:
            tree_map = file.read().split('\n')
            self.assertEqual(2, count_trees(tree_map, 1, 2))

    def test_example_multiply(self):
        with open('test_input.txt') as file:
            tree_map = file.read().split('\n')
            self.assertEqual(336, multiply(tree_map))

    def test_original_multiply(self):
        with open('input.txt') as file:
            tree_map = file.read().split('\n')
            mul = multiply(tree_map)
            self.assertEqual(2431272960, mul)
