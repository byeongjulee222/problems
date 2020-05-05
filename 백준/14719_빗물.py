import sys; sys.stdin = open('txt/14719_빗물.txt', 'r')

def left(a, b):
    while b >= 0:
        if not board[a][b]:
            b -= 1
            continue
        elif board[a][b]:
            return 1
    return False

def right(a, b):
    while b < x:
        if not board[a][b]:
            b += 1
            continue
        elif board[a][b]:
            return 1
    return False

for _ in range(int(input())):
    y, x = map(int, input().split())
    arr = list(map(int, input().split()))
    board = [list(0 for _ in range(x)) for _ in range(y)]
    for i in range(x):
        for j in range(arr[i]):
            board[j][i] = 1

    cnt = 0
    for i in range(y):
        for j in range(x):
            if not board[i][j]:
                score = left(i, j) + right(i, j)
                if score == 2:
                    cnt += 1

    print(cnt)