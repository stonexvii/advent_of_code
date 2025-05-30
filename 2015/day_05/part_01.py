VOWELS = 'aeiou'
FORBIDDEN_SEQUENCES = {'ab', 'cd', 'pq', 'xy'}


def read_data(path: str):
    with open(path, 'r', encoding='UTF-8') as file:
        data = [line.strip() for line in file.readlines()]
    return data


def solution(path: str):
    data = read_data(path)
    result = 0
    for line in data:
        vowels_count = 0
        for ch in line:
            if ch in VOWELS:
                vowels_count += 1
            if vowels_count == 3:
                break
        else:
            continue
        for idx in range(len(line) - 1):
            if line[idx] == line[idx + 1]:
                break
        else:
            continue
        for sequence in FORBIDDEN_SEQUENCES:
            if sequence in line:
                break
        else:
            result += 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
