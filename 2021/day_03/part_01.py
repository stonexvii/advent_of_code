from copy import deepcopy


def read_data(path: str):
    with open(path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def solution(path: str):
    puzzle_data = read_data(path)
    oxygen = list(zip(*puzzle_data))
    co2 = deepcopy(oxygen)

    def collect_oxygen(data: list[list[int]], idx=0):
        if len(data) == 1:
            return data
        ones = []
        for i in range(len(data)):
            if data[i][idx] == 1:
                ones.append(i)
        if len(ones) > (len(data) - len(ones)):
            indexes = ones.copy()
        else:
            indexes = set(range(len(data))).difference(set(ones))
        for i in indexes:
            data.pop(i)
        return collect_oxygen(data, idx + 1)

    def collect_co2(data: list[list[int]], idx=0):
        if len(data) == 1:
            return data
        ones = []
        for i in range(len(data)):
            if data[i][idx] == 1:
                ones.append(i)
        if len(ones) < (len(data) - len(ones)):
            indexes = ones.copy()
        else:
            indexes = set(range(len(data))).difference(set(ones))
        for i in indexes:
            data.pop(i)
        return collect_co2(data, idx + 1)

    oxygen = collect_oxygen(oxygen)
    co2 = collect_co2(co2)
    return oxygen * co2


if __name__ == '__main__':
    print(solution('input_data.txt'))
