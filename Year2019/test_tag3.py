from unittest import TestCase

from tag3 import manhattan, move_right, compute_positions, steps, compute_steps


class Test(TestCase):
    def test_move_in_x(self):
        position = (0, 0)
        positions = [position]
        positions = move_right(positions, "R2")
        assert positions == [(0, 0), (1, 0), (2, 0)], "Expected: [(1,0), (2,0)], but was + " + str(positions)

    def test1(self):
        wire1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
        wire2 = ["U62", "R66", "U55", "R34", "D71", "R55",
                 "D58", "R83"]
        distance = manhattan(wire1, wire2)
        assert distance == 159, "Expected 159, but was " + str(distance)

    def test2(self):
        wire1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
        wire2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
        distance = manhattan(wire1, wire2)
        assert distance == 135, "Expected 135, but was " + str(distance)

    def test3(self):
        wire1 = ["R8", "U5", "L5", "D3"]
        wire2 = ["U7", "R6", "D4", "L4"]

        distance = manhattan(wire1, wire2)
        assert distance == 6, "Expected 6, but was " + str(distance)

    def test_compute_positions(self):
        wire = ["R2", "D2", "L2", "U2"]
        expected_positions = [(0, 0), (1, 0), (2, 0), (2, -1), (2, -2), (1, -2), (0, -2), (0, -1), (0, 0)]
        positions = [(0, 0)]
        compute_positions(positions, wire)

        assert positions == expected_positions, "Expected " + str(expected_positions) + ", but was " + str(positions)

    def test_steps(self):
        wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
        wire2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

        count = steps(wire1, wire2)
        assert count == 610, "Expected 610, but was " + str(count)

    def test_steps2(self):
        wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
        wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")

        count = steps(wire1, wire2)
        assert count == 410, "Expected 410, but was " + str(count)

    def test_steps3(self):
        wire1 = "R8,U5,L5,D3".split(",")
        wire2 = "U7,R6,D4,L4".split(",")

        count = steps(wire1, wire2)
        assert count == 30, "Expected 30, but was " + str(count)

    def test_step_reduce(self):
        wire = "R991,U77,L916,D78".split(",")
        position = compute_steps(wire)

        assert position[(991 - 916, -1)] == 991 + 916 + 77 + 78, "Expected " + str(991 + 916 + 77 + 78) + ", but was " + str(
            position[(991 - 916, -1)])
        assert position[(991-916, 1)] == 991+77+916+76, "Expected " + str(991+77+916+76) + ", but was " + str(
            position[(991 - 916, 1)])
        assert position[(991, 0)] == 991, "Expected 991, but was " + str(position[(991, 0)])
