from itertools import combinations


def read_data(path: str):
    with open(path, 'r') as file:
        return list(map(int, file.readlines()))


def solution(path: str, total: int):
    result = 0
    data = read_data(path)
    for l in range(1, len(data)):
        for i in combinations(data, r=l):
            if sum(i) == total:
                result += 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt', 150))
