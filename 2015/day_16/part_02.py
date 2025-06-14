target_aunt = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def read_data(path: str):
    auntie = {}
    with open(path, 'r') as file:
        for line in file.readlines():
            aunt, values = line.split(': ', 1)
            auntie[aunt] = {}
            for line_value in values.split(', '):
                key, value = line_value.split(': ')
                auntie[aunt][key] = int(value)
    return auntie


def solution(path: str):
    auntie_data = read_data(path)
    for aunt, options in auntie_data.items():
        the_necessary_aunt = []
        for parameter, value in options.items():
            if parameter in ('cats', 'trees'):
                the_necessary_aunt.append(target_aunt[parameter] <= value)
            elif parameter in ('pomeranians', 'goldfish'):
                the_necessary_aunt.append(target_aunt[parameter] >= value)
            else:
                the_necessary_aunt.append(target_aunt[parameter] == value)
        if all(the_necessary_aunt):
            return aunt


if __name__ == '__main__':
    print(solution('input_data.txt'))
