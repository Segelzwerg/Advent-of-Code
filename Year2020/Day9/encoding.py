class Preamble:
    def __init__(self, values: [int]):
        self.values: [int] = values

    def next(self, value: int):
        for x in self.values:
            for y in self.values:
                if x + y == value:
                    self.values.pop(0)
                    self.values.append(value)
                    return None
        return value


def load_data(filename='input.txt'):
    with open(filename) as file:
        values = [int(number) for number in file.read().split('\n')]
        return values


def find_first(values, preamble_length=25):
    preamble = Preamble(values[:preamble_length])

    index = preamble_length
    while preamble.next(values[index]) is None:
        index += 1

    return values[index]


def find_set(values, number, start_index=0):
    value_set = values[start_index:start_index + 2]
    index = start_index + 2
    while sum(value_set) < number:
        value_set.append(values[index])
        index += 1
    if sum(value_set) == number:
        return min(value_set), max(value_set)
    else:
        return find_set(values, number, start_index + 1)


if __name__ == '__main__':
    test_values = load_data('test_input.txt')
    values = load_data('input.txt')
    test_number = find_first(test_values, preamble_length=5)
    number = find_first(values)
    set_min, set_max = find_set(test_values, test_number)
    print(f'{set_min}+{set_max}={set_min + set_max}')
    set_min, set_max = find_set(values, number)
    print(f'{set_min}+{set_max}={set_min + set_max}')
