from string import ascii_letters


def read_data(path: str):
    with open(path, 'r') as file:
        while line := file.readline():
            a, b, c, d = map(int, line.strip().replace(',', ' ').replace('-', ' ').split(' '))
            yield a, b, c, d


def create_range(start: int, stop: int):
    return set(range(start, stop + 1))


def solution(path: str):
    result = 0
    for a, b, c, d in read_data(path):
        first = create_range(a, b)
        second = create_range(c, d)
        if not first.isdisjoint(second):
            result += 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
