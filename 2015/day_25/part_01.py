def solution(line, position):
    counter = 20151125
    matrix = []
    row = 0
    line -= 1
    position -= 1
    while True:
        for k in range(row, -1, -1):
            if len(matrix) <= row:
                matrix.append([counter])
            else:
                matrix[k].append(counter)
            counter *= 252533
            counter %= 33554393
            if len(matrix) > line and len(matrix[line]) > position:
                return matrix[line][position]
        row += 1


if __name__ == '__main__':
    print(solution(2978, 3083))
