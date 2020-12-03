import numpy

TREE = '#'


def count_trees(tree_map, right_move, move_down=1) -> int:
    width = len(tree_map[0])
    x_pos = 0
    big_string = ""
    print('\n')
    for row in tree_map[0::move_down]:
        row = list(row)
        if row[x_pos] == TREE:
            row[x_pos] = 'X'
        else:
            row[x_pos] = 'O'
        row = "".join(row)
        big_string = big_string + row
        x_pos = (x_pos + right_move) % width

    return big_string.count('X')


def multiply(tree_map) -> int:
    trees = [count_trees(tree_map, move_right) for move_right in [1, 3, 5, 7]]
    trees.append(count_trees(tree_map, 1, 2))
    return numpy.product(trees)


def main():
    with open('input.txt') as file:
        tree_map = file.read().split('\n')
        print(count_trees(tree_map, 3))
        print(multiply(tree_map))


if __name__ == '__main__':
    main()
