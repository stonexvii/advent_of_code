def read_data(path: str):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            if line != '\n':
                left, right = line.strip().split('-')
                result.extend([(int(left), 'L'), (int(right), 'R')])
            else:
                break
    return result


def solution(path: str):
    result, left_limits, data = 0, [], sorted(read_data(path))
    for number, letter in data:
        if letter == 'L':
            left_limits.append(number)
        else:
            item = left_limits.pop()
            if not left_limits:
                result += (number - item) + 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
