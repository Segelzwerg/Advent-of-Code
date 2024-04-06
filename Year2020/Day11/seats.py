class Seat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.changed = True
        self.seated = False
        self.neighbors: ['Seat'] = []
        self.next_state = None

    def __str__(self):
        if self.seated:
            return '#'
        return 'L'

    def __repr__(self):
        return f'{self}({self.x},{self.y})'

    def add_neighbor(self, neighbor: 'Seat'):
        self.neighbors.append(neighbor)

    def new_state(self, leave_thres):
        if not self.seated and all(neighbor.seated is False for neighbor in self.neighbors):
            self.next_state = True
            self.changed = True
        elif (self.seated and
              len([neighbor for neighbor in self.neighbors if
                   neighbor.seated is True]) >= leave_thres):
            self.next_state = False
            self.changed = True
        else:
            self.changed = False
            self.next_state = self.seated


def next_round(seats: [Seat], leave_thres: int) -> [Seat]:
    for seat in seats:
        seat.new_state(leave_thres)
    return seats


def find_stable(seats: [Seat], leave_thres=4) -> int:
    counter = 1
    while any(seat.changed is True for seat in seats):
        seats = next_round(seats, leave_thres)
        for seat in seats:
            seat.seated = seat.next_state
        print(f'Done with round #{counter}')
        counter += 1
    return len([seat for seat in seats if seat.seated])


def load_data(filename: str) -> [Seat]:
    with open(filename) as file:
        seats: [Seat] = []
        rows = file.read().split('\n')
        for y, row in enumerate(rows):
            for x, tile in enumerate(row):
                if tile == 'L':
                    new_seat = Seat(x, y)
                    neighbors = [seat for seat in seats if (x - 1 <= seat.x <= x + 1) and
                                 (y - 1 <= seat.y <= y + 1)]
                    for neighbor in neighbors:
                        new_seat.add_neighbor(neighbor)
                        neighbor.add_neighbor(new_seat)
                    seats.append(new_seat)

        return seats


def load_data2(filename: str) -> [Seat]:
    with open(filename) as file:
        seats: [Seat] = []
        rows = file.read().split('\n')
        for y, row in enumerate(rows):
            for x, tile in enumerate(row):
                if tile == 'L':
                    seats.append(Seat(x, y))
        return seats


if __name__ == '__main__':
    test_seats = load_data('test_input.txt')
    # print(find_stable(test_seats))
    test_data = load_data2('test_input.txt')
    x_max = max([seat.x for seat in test_data])
    test_seats2 = get_neighbors(test_data, x_max)
    print(find_stable(test_seats2, 5))
    # seats = load_data('input.txt')
    # print(find_stable(seats))
    # print(find_stable(seats, 5))
