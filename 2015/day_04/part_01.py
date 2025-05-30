from hashlib import md5

in_data = 'bgvyzdsv'


def solution(data):
    idx = 0
    while True:
        new_hash = md5((in_data + str(idx)).encode()).hexdigest()
        if new_hash.startswith('00000'):
            return data + str(idx)
        idx += 1


if __name__ == '__main__':
    print(solution(in_data))
