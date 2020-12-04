REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
VALID_EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def get_passports(text_input: list):
    passports = [passport.replace('\n', ' ').replace(' ', ', ') for passport in text_input]
    passports_dicts = []
    for passport in passports:
        passport = dict(
            (x, y) for x, y in (element.split(':') for element in passport.split(', ')))
        passports_dicts.append(passport)

    return passports_dicts


def _check_parameter(passport):
    byr = int(passport['byr'])
    iyr = int(passport['iyr'])
    eyr = int(passport['eyr'])
    hgt = passport['hgt']
    hcl = passport['hcl']
    ecl = passport['ecl']
    pid = passport['pid']
    if not 1920 <= byr <= 2002:
        return False
    if not 2010 <= iyr <= 2020:
        return False
    if not 2020 <= eyr <= 2030:
        return False
    if not (len(pid) == 9 and pid.isdecimal()):
        return False
    if not any(ecl == color for color in VALID_EYE_COLORS):
        print(passport['ecl'])

        return False
    if hgt.endswith('cm'):
        height = int(hgt.rstrip('cm'))
        if not 150 <= height <= 193:
            return False
    if hgt.endswith('in'):
        height = int(hgt.rstrip('in'))
        if not 59 <= height <= 76:
            return False
    if not (hgt.endswith('cm') or hgt.endswith('in')):
        return False

    if not (hcl.startswith('#') and len(hcl) == 7):
        return False
    return True


def count_valids(passports) -> int:
    counter = len(passports)
    for passport in passports:
        keys: list = passport.keys()
        if not _check_keys(keys):
            counter -= 1
        else:
            if not _check_parameter(passport):
                counter -= 1

    return counter


def _check_keys(keys):
    for required_key in REQUIRED_KEYS:
        if required_key not in keys:
            return False
    return True


def main():
    with open('input.txt') as file:
        text_input = file.read().split('\n\n')
        passports = get_passports(text_input)
        print(count_valids(passports))


if __name__ == '__main__':
    main()
