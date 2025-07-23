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
    validated_data = []
    for i in range(len(address) - 2):
        data = address[i:i + 3]
        if data[0] == data[2] and len(set(data)) == 2:
            validated_data.append(data[1] + data[0] + data[1])
    return validated_data

def check_filter(address_filter: str, address_list: list[str]) -> bool:
    for address in address_list:
        if address_filter in address:
            return True
    return False


def solution(path: str) -> int:
    count = 0
    for full_address in read_data(path):
        skip = False
        for address in full_address.outer:
            if filters := validator(address):
                for address_filter in filters:
                    if check_filter(address_filter, full_address.inner):
                        count += 1
                        skip = True
                        break
            if skip:
                break
    return count


if __name__ == '__main__':
    print(solution('input_data.txt'))
