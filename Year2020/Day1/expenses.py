def expenses(input: [int]):
    for x in input:
        for y in input:
            if x + y == 2020:
                print(f'x={x}, y={y}')
                return x * y
