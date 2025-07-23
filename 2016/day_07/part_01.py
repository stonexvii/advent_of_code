from collections import namedtuple

Data = namedtuple('Data', ['outer', 'inner'])


def read_data(path: str):
    data = []
    with open(path, 'r') as file:
        for address in file:
            address = address.strip().replace('[', ' ').replace(']', ' ').split()
            data.append(Data(address[::2], address[1::2]))
    return data


def validator(address: str):
    for i in range(len(address) - 3):
        data = address[i:i + 4]
        if data[:2] == data[2:][::-1] and len(set(data)) == 2:
            return True
    return False


def solution(path: str) -> int:
    count = 0
    for full_address in read_data(path):
        skip = False
        for address in full_address.inner:
            if validator(address):
                skip = True
                break
        if skip:
            continue
        for address in full_address.outer:
            if validator(address):
                count += 1
                break
    return count


if __name__ == '__main__':
    print(solution('input_data.txt'))
