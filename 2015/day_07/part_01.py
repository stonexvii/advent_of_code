from itertools import zip_longest


def bin_gen(number: int):
    bin_number = list(f'{number:0b}')
    while bin_number:
        yield int(bin_number.pop())
    return 0

def bor(a: int, b: int):
    result = ''
    next_a = bin_gen(a)
    next_b = bin_gen(b)
    while next_a or next_b:
        result += str(next(next_a) + next(next_b))
    return result

print(bor(23, 34))

# def bor(a: int, b: int):
#     res = ''
#     for i, j in zip_longest(f'{a:0b}'[::-1], f'{b:0b}'[::-1], fillvalue=0):
#         res += str(int(bool(int(i) + int(j))))
#     return int(res[::-1], 2)
#
#
# def band(a: int, b: int):
#     res = ''
#     for i, j in zip_longest(f'{a:0b}'[::-1], f'{b:0b}'[::-1], fillvalue=0):
#         res += str(int(bool(int(i) * int(j))))
#     return int(res[::-1], 2)

for i in bin_gen(34):
    print(i)

