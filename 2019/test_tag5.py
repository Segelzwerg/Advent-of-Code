from unittest import TestCase
import tag5


class Test(TestCase):
    def test_gravity_assist(self):
        opcode = [1002, 4, 3, 4, 33]
        tag5.gravity_assist(opcode)
        assert opcode[4] == 99, "Expected 99, but was " + str(opcode[3])

    def test_part_2(self):
        opcode = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                  1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                  999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        tag5.gravity_assist(opcode)

    def test_1(self):
        opcode = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        tag5.gravity_assist(opcode)

    def test_2(self):
        opcode = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        tag5.gravity_assist(opcode)

    def test_3(self):
        opcode = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        tag5.gravity_assist(opcode)
