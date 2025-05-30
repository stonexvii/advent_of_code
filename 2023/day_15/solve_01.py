def data_reader(path: str) -> list[str]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    return data[0]

def check_hash(string_data: str) -> int:
    result = 0
    for ch in string_data:
        result += ord(ch)
        result *= 17
        result %= 256
    return result

def solution(data: str) -> int:
    result = 0
    for item in data.strip().split(','):
        print(i_hash := check_hash(item))
        result += i_hash

    return result

if __name__ == '__main__':

    test = 'rn,cm,qp,cm,qp,pc,ot,ab,pc,pc,ot'
    data = data_reader('input_data.txt')
    print(solution(test))

