import sys; sys.stdin = open("1974_sudoku.txt", "r")

T = int(input())
for TC in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # print(arr)
    cnt = 0
    SUM_x = 0
    SUM_y = 0
    for i in range(9):
        for j in range(9):
            SUM_x += arr[i][j]
            SUM_y += arr[j][i]
        if SUM_x == 45:
            cnt += 1
        if SUM_y == 45:
            cnt += 1
        print(cnt)

    SUM_b = 0
    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            for i in range(3):
                for j in range(3):
                    SUM_b += arr[i+k][j+l]
                if SUM_b == 45:
                    cnt += 1
    if cnt == 27:
        print(1)
    else:
        print(0)