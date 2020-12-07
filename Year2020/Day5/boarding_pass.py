from math import floor

import numpy


def determine_row(rows: str, lowest: int = 0, highest: int = 127) -> int:
    if len(rows) >= 1:
        section = rows[0]
        rows = rows[1:]

        mid = lowest + floor((highest - lowest) / 2)
        if section == 'F':
            highest = mid
        elif section == 'B':
            lowest = mid + 1
        else:
            raise ValueError('section was neither "F" nor "B".')

        return determine_row(rows, lowest, highest)
    else:
        # sanity check
        if lowest == highest:
            return lowest
        else:
            raise ValueError(f'lowest: {lowest} != highest {highest}')


def determine_column(columns, lowest: int = 0, highest: int = 7) -> int:
    if len(columns) >= 1:
        section = columns[0]
        columns = columns[1:]

        mid = lowest + floor((highest - lowest) / 2)
        if section == 'L':
            highest = mid
        elif section == 'R':
            lowest = mid + 1
        else:
            raise ValueError('section was neither "L" nor "R".')

        return determine_column(columns, lowest, highest)
    else:
        # sanity check
        if lowest == highest:
            return lowest
        else:
            raise ValueError(f'lowest: {lowest} != highest {highest}')


def load_data(input_txt='input.txt'):
    data = numpy.genfromtxt(input_txt, dtype=str)
    data = [(row[0:7], row[7:]) for row in data]
    return data


def get_seat_id(boarding_pass):
    row = determine_row(boarding_pass[0])
    column = determine_column(boarding_pass[1])
    return 8 * row + column


def main():
    data = load_data()
    seat_ids = [get_seat_id(boarding_pass) for boarding_pass in data]
    highest_seat_id = max(seat_ids)
    lowest_seat_id = min(seat_ids)

    print(highest_seat_id)
    print(lowest_seat_id)

    seat_ids.sort()
    for current, next in zip(seat_ids[0:-1], seat_ids[1:]):
        if not current + 1 == next:
            print(current+1)
            break


if __name__ == '__main__':
    main()
