import numpy as np


def password_valid(policy: str, password: str) -> bool:
    limit = policy[0].split('-')
    amount = password.count(policy[1])
    return int(limit[0]) <= amount <= int(limit[1])


def password_valid2(policy: [str, str], password: str) -> bool:
    positions = policy[0].split('-')
    first_pos = int(positions[0]) - 1
    second_pos = int(positions[1]) - 1
    character = policy[1]
    return ((password[first_pos] == character) !=
            (password[second_pos] == character))


def load_input():
    input_array = np.genfromtxt('input.txt', delimiter=':', dtype=str)
    policies = np.array([policy.split(' ') for policy in input_array.T[0]])
    passwords = [password.strip() for password in input_array.T[1]]

    return policies, passwords


def count_valids(policies, passwords):
    counter = 0
    for policy, password in zip(policies, passwords):
        if password_valid(policy, password):
            counter += 1
    return counter


def count_valids2(policies, passwords):
    counter = 0
    for policy, password in zip(policies, passwords):
        if password_valid2(policy, password):
            counter += 1
    return counter


def print_valids2(policies, passwords):
    for policy, password in zip(policies, passwords):
        if password_valid2(policy, password):
            print(f'{policy}: {password}')


def main():
    policies, passwords = load_input()
    print(count_valids(policies, passwords))
    print(count_valids2(policies, passwords))
    print_valids2(policies, passwords)


if __name__ == '__main__':
    main()
