from itertools import groupby
from string import ascii_lowercase as alpha

for let in 'iol':
    alpha = alpha.replace(let, '')


def solution(password: str) -> str:
    if any(map(lambda x: x in password, 'iol')):
        min_idx = min([password.find(i) for i in 'iol' if password.find(i) != -1]) + 1
        password = password[:min_idx].replace('i', 'j').replace('o', 'p').replace('l', 'm') + 'a' * (8 - min_idx)
    password = list(password)
    idx = len(password) - 1
    while idx:
        if password[idx] == 'z':
            password[idx] = 'a'
            idx -= 1
        while password[idx] != 'z':
            password[idx] = alpha[(alpha.index(password[idx]) + 1) % len(alpha)]
            idx = len(password) - 1
            joined_password = ''.join(password)
            for i in range(len(joined_password) - 3):
                if joined_password[i:i + 3] in alpha:
                    result = set()
                    skip = False
                    for n, k in groupby(joined_password, key=lambda x: x[0]):
                        if skip:
                            skip = False
                            continue
                        k = len(list(k))
                        if k >= 2:
                            result.add((n, k))
                            skip = True
                    if len(result) >= 2:
                        return joined_password


if __name__ == '__main__':
    print(solution('hxbxxyzz'))

