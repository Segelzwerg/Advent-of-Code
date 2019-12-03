from unittest import TestCase

from tag3 import manhattan


class Test(TestCase):
    def test_move_in_x(self):
        self.fail()

    def test1(self):
        wire1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
        wire2 = ["U62", "R66", "U55", "R34", "D71", "R55",
                 "D58", "R83"]
        distance = manhattan(wire1, wire2)
        assert distance == 159, "Expectec 159, but was " + str(distance)

    def test2(self):
        wire1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
        wire2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
        distance = manhattan(wire1, wire2)
        assert distance == 135, "Expectec 135, but was " + str(distance)
