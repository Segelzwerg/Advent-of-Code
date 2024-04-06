from Year2020.Day10.adapter import load_data


class Adapter():
    def __init__(self, value):
        self.value = value
        self.arrangements = 0

    def __repr__(self):
        return f'{self.value}:{self.arrangements}'


if __name__ == '__main__':
    values = load_data('input.txt')
    values.append(0)
    values.sort()
    values.append(values[-1]+3)
    adapters = [Adapter(value) for value in values]
    arrangements = 0
    for index, adapter in enumerate(adapters):
        previous = [prev for prev in adapters[max(0, index - 3):max(0, index)]
                    if prev.value >= adapter.value - 3]
        adapter.arrangements = max(1, sum([prev.arrangements for prev in previous]))
        print(f'{previous}={adapter}')

    print(adapters[-1].arrangements)
