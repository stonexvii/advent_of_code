combinations = {
    'A': {
        'X': 4,
        'Y': 8,
        'Z': 3,
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9,
    },
    'C': {
        'X': 7,
        'Y': 2,
        'Z': 6,
    }
}


def read_data(path: str):
    with open(path, 'r') as file:
        return [line.strip().split(' ') for line in file.readlines()]


def solution(path: str):
    return sum([combinations[a][b] for a, b in read_data(path)])


if __name__ == '__main__':
    print(solution('input_data.txt'))
