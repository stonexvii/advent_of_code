from part_01 import read_data


def solution(path: str):
    data = read_data(path)
    result = 0
    for line in data:
        for idx in range(len(line) - 1):
            if line[idx:idx + 2] in line[:idx] + ' ' + line[idx + 2:]:
                break
        else:
            continue
        for idx in range(len(line) - 2):
            if line[idx] == line[idx + 2]:
                break
        else:
            continue
        result += 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
