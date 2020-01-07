def Star(x, y, num):
    if num == 1:
        matrix[x][y] = '*'
        return

    div = num // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                pass
            else:
                Star(x + (i * div), y + (j * div), div)

matrix = [[' '] * 2188 for i in range(2188)]
N = int(input())

Star(0, 0, N)

for i in range(N):
    string = ''
    for j in range(N):
        string += matrix[i][j]
    print(string)


print(3**7)