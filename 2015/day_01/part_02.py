from part_01 import read_data


def solution(path: str):
    data = read_data(path)
    floor = 0
    for idx, ch in enumerate(data, 1):
        floor += 1 if ch == '(' else -1
        if floor == -1:
            return idx


print(solution('input_data.txt'))
