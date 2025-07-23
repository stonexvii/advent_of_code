from collections import Counter


def read_data(path: str):
    with open(path, 'r') as file:
        return list(map(lambda x: x.strip(), file))


def solution(path: str):
    messages = [Counter(message).most_common(1) for message in zip(*read_data(path))]
    return ''.join(list(map(lambda x: x[0][0], messages)))


if __name__ == '__main__':
    print(solution('input_data.txt'))
