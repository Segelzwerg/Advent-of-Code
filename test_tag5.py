from unittest import TestCase
import tag5


class Test(TestCase):
    def test_gravity_assist(self):
        opcode = [1002, 4, 3, 4, 33]
        tag5.gravity_assist(opcode)
        assert opcode[4] == 99, "Expected 99, but was " + str(opcode[3])
