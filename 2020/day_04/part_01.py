PATTERN = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}


def list_to_dict(passport_data: list[str]):
    passport = {}
    for line in passport_data:
        key, value = line.split(':')
        passport[key] = value
    return passport


def read_data(path: str):
    data, passport = [], ''
    with open(path, 'r') as file:
        while line := file.readline():
            if line != '\n':
                passport += line
            else:
                data.append(list_to_dict(passport.replace('\n', ' ').split()))
                passport = ''
        data.append(list_to_dict(passport.replace('\n', ' ').split()))
    return data


def solution(path: str):
    result = 0
    for line in read_data(path):
        if PATTERN.issubset(set(line)):
            result += 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
    # print({1, 2}.issubset({1, 2, 3}))
