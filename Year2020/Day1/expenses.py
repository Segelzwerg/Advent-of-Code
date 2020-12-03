import numpy as np


def expenses(input_array: [int]):
    for x in input_array:
        for y in input_array:
            if x + y == 2020:
                print(f'x={x}, y={y}')
                return x * y


def three_sum(input_array: [int]) -> int:
    for x in input_array:
        for y in input_array:
            for z in input_array:
                if x + y + z == 2020:
                    print(f'x={x}, y={y}, z={z}')
                    return x * y * z


def main():
    input_array = np.genfromtxt('input.txt', dtype=int)
    print(expenses(input_array))
    print(three_sum(input_array))


if __name__ == '__main__':
    main()
