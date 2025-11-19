from string import ascii_letters


def read_data(path: str):
    with open(path, 'r') as file:
        while line := file.readline():
            line = line.strip()
            yield line[:len(line) // 2], line[len(line) // 2:]


def check_letter(words: tuple[str, str]):
    for ch in set(words[0]):
        if ch in set(words[1]):
            return ch


def solution(path: str):
    result = 0
    for line in read_data(path):
        result += ascii_letters.index(check_letter(line)) + 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
