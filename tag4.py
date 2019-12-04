def has_double_digits(password):
    password = str(password)

    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return True

    return False


def is_incremental(password):
    password = str(password)
    for i in range(len(password)-1):
        if int(password[i]) > int(password[i+1]):
            return False

    return True


def is_legit(password):
    if not has_double_digits(password):
        return False
    if not is_incremental(password):
        return False

    return True


def count_legit_pwds(lower_limit, upper_limit):
    current = lower_limit
    counter = 0
    while current <= upper_limit:
        if is_legit(current):
            counter += 1
        current += 1
    return counter


if __name__ == '__main__':
    lower_limit = 128392
    upper_limit = 643281

    print(count_legit_pwds(lower_limit, upper_limit))