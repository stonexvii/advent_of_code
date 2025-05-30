from itertools import groupby


def solution(start_number: int, iterations: int) -> int:
    for _ in range(iterations):
        new_number = ''
        for number, ratio in groupby(str(start_number)):
            new_number += f'{len(list(ratio))}{number}'
        start_number = new_number
    return len(start_number)


if __name__ == '__main__':
    print(solution(1321131112, 50))
