def read_data(path: str):
    result = [[], []]
    idx = 0
    with open(path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                if idx:
                    result[idx].append(int(line))
                else:
                    left, right = map(int, line.split('-'))
                    result[idx].append((left, right))
            else:
                idx += 1
    return result


def solution(path: str):
    result = 0
    limits, products = read_data(path)
    for product in products:
        for left, right in limits:
            if left <= product <= right:
                result += 1
                break
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
