combinations = {
    'A': {
        'X': 3,
        'Y': 4,
        'Z': 8,
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9,
    },
    'C': {
        'X': 2,
        'Y': 6,
        'Z': 7,
    }
}


def read_data(path: str):
    with open(path, 'r') as file:
        return [line.strip().split(' ') for line in file.readlines()]


def solution(path: str):
    return sum([combinations[a][b] for a, b in read_data(path)])


if __name__ == '__main__':
    print(solution('input_data.txt'))
