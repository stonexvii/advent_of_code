from collections import namedtuple
from collections import Counter
from string import ascii_lowercase

Data = namedtuple('Data', ['sequence', 'id', 'summa'])


def read_data(path: str):
    result = []
    with open(path, 'r') as file:
        for line in file:
            seq, summa = line.strip().rsplit('-', 1)
            num_id, summa = summa.split('[')
            result.append(Data(seq, int(num_id), summa[:-1]))
    return result


def ceaser_cipher(word: str, key: int):
    cipher_word = ''
    for letter in word:
        if letter == '-':
            cipher_word += ' '
        else:
            cipher_word += ascii_lowercase[(ascii_lowercase.index(letter) + key) % len(ascii_lowercase)]
    return cipher_word


def solution(path: str):
    for room in read_data(path):
        true_room = ceaser_cipher(room.sequence, room.id)
        if 'northpole' in true_room:
            return room.id


if __name__ == '__main__':
    print(solution('input_data.txt'))
