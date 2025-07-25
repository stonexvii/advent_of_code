from string import ascii_uppercase
from functools import reduce
from operator import mul


def read_data(path: str):
    with open(path, 'r') as file:
        return file.read()


def split_marker(item: str):
    item = item.replace('(', ' ').replace(')', ' ').split()
    item = tuple(map(lambda x: x.split('x'), item))
    cnt = reduce(mul, map(lambda x: int(x[1]), item))
    print(int(item[-1][0]), cnt)
    return int(item[-1][0]), cnt


def next_index(word: str):
    print('word', word)
    for i in range(len(word)):
        if word[i].isupper():
            print(i)
            return i


def solution(path: str):
    data = read_data(path)
    uncompressed = ''
    i = 0
    while i < len(data):
        print(uncompressed[-80:], data[i], i)
        if data[i] != '(':
            uncompressed += data[i]
            i += 1
        else:
            idx_closed = i + next_index(data[i:]) - 1
            slc, cnt = split_marker(data[i:idx_closed+1])
            next_idx = idx_closed + 1
            for _ in range(cnt):
                uncompressed += data[next_idx:next_idx + slc]
            i = next_idx + slc
        print(uncompressed)
    return len(uncompressed)


if __name__ == '__main__':
    print(solution('test_data.txt'))
