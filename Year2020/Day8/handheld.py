from copy import deepcopy


class Instruction:
    def __init__(self, cmd, param):
        self.cmd = cmd
        self.param = int(param)
        self.executed = False

    def __repr__(self):
        return f'Instruction: {self.cmd}: {self.param}'

    def execute(self, index: int, acc: int):
        self.executed = True
        if self.cmd == 'nop':
            return index + 1, acc
        elif self.cmd == 'acc':
            return index + 1, acc + self.param
        elif self.cmd == 'jmp':
            return index + self.param, acc
        else:
            raise ValueError(f'{self.cmd} is not valid command')


def load_data(filename: str):
    with open(filename) as file:
        data = [line.split(' ') for line in file.read().split('\n')]
        instructions = [Instruction(line[0], line[1]) for line in data]
        return instructions


def run_instruction(instructions) -> [int, bool]:
    acc = 0
    index = 0
    instruction = instructions[index]
    while not instruction.executed:
        index, acc = instruction.execute(index, acc)
        if index >= len(instructions):
            return acc, True
        instruction = instructions[index]

    return acc, False


def part_1(filename='input.txt'):
    instructions = load_data(filename)
    print(run_instruction(instructions)[0])


def flip(base_instructions, index):
    instructions = deepcopy(base_instructions)
    if instructions[index].cmd == 'nop':
        instructions[index] .cmd= 'jmp'
    elif instructions[index].cmd == 'jmp':
        instructions[index].cmd = 'nop'
    return instructions


def switch_instructions(instructions, index):
    instruction = instructions[index]
    while instruction.cmd != 'nop' and instruction.cmd != 'jmp' and index < len(instructions)-1:
        index += 1
        instruction = instructions[index]
    instructions = flip(instructions, index)
    return instructions, index+1


def part_2(filename='input.txt'):
    instructions = load_data(filename)
    base_instructions = instructions.copy()
    terminated = False
    acc = None
    index = 0
    while not terminated:
        instructions, index = switch_instructions(base_instructions, index)
        acc, terminated = run_instruction(instructions)

    return acc


if __name__ == '__main__':
    part_1('test.txt')
    part_1()
    part_2('test.txt')
    print(part_2())
