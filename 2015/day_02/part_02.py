from part_01 import read_data
from itertools import combinations
from functools import reduce


def solution(path: str):
    data = read_data(path)
    result = 0
    for entry in data:
        min_entry = min(combinations(entry, 2), key=lambda x: x[0] + x[1])
        result += sum(min_entry) * 2 + reduce(lambda x, y: x * y, entry)
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
