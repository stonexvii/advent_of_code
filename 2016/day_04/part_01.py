from collections import namedtuple
from collections import Counter

Data = namedtuple('Data', ['sequence', 'id', 'summa'])


def read_data(path: str):
    result = []
    with open(path, 'r') as file:
        for line in file:
            seq, summa = line.strip().rsplit('-', 1)
            num_id, summa = summa.split('[')
            seq = seq.replace('-', '')
            result.append(Data(seq, int(num_id), summa[:-1]))
    return result


def solution(path: str):
    total = 0
    for line in read_data(path):
        seq = Counter(line.sequence).most_common()
        seq = sorted(sorted(seq, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
        line_summa = ''.join(list(map(lambda x: x[0], seq[:5])))
        if line.summa == line_summa:
            total += line.id
    return total


if __name__ == '__main__':
    print(solution('input_data.txt'))
