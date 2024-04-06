import copy
from typing import Union


def load_data(filename: str):
    with open(filename) as file:
        return [int(number) for number in file.read().split('\n')]


def find_differences(adapters: [int]) -> [int, int]:
    rating = 0
    difference_one = 0
    difference_three = 0
    own_device = max(adapters) + 3
    adapters.append(own_device)
    while (possible_adapter := find_adapter(adapters, rating)) is not None:

        if possible_adapter - rating == 1:
            difference_one += 1
        elif possible_adapter - rating == 3:
            difference_three += 1
        adapters.remove(possible_adapter)
        rating = possible_adapter
    return difference_one, difference_three


def find_adapter(adapters, rating) -> Union[int, None]:
    possible_adapters = find_adapters(adapters, rating)
    if len(possible_adapters) == 0:
        return None
    return min(possible_adapters)


def find_adapters(adapters, rating):
    return [adapter for adapter in adapters if 1 <= adapter - rating <= 3]


def part_1(adapters: [int]) -> None:
    diff_one, diff_three = find_differences(adapters)
    print(f'{diff_one}*{diff_three}={diff_one * diff_three}')


def find_arrangements(adapters: [int], rating: int = 0) -> int:
    own_device = max(adapters) + 3
    adapters.append(own_device)
    amount_arrangements = 0
    while len(possible_adapters := find_adapters(adapters, rating)) > 0:
        for adapter in possible_adapters[1:]:
            amount_arrangements += 1
            amount_arrangements += find_arrangements(copy.deepcopy(adapters), adapter)
        adapters.remove(possible_adapters[0])
        rating = possible_adapters[0]
    return amount_arrangements


if __name__ == '__main__':
    part_1(load_data('small_test_input.txt'))
    part_1(load_data('large_test_input.txt'))
    part_1(load_data('input.txt'))
    print(find_arrangements(load_data('small_test_input.txt'))+1)
    print(find_arrangements(load_data('large_test_input.txt'))+1)
    print(find_arrangements(load_data('input.txt'))+1)
