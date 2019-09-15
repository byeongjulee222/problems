import sys; sys.stdin = open("txt/1974_sudoku.txt", "r")

T = int(input())
for TC in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0
    for i in range(9):
        SUM_x = SUM_y = 0
        for j in range(9):
            SUM_x += arr[i][j]
            SUM_y += arr[j][i]
        if SUM_x == 45:
            cnt += 1
        if SUM_y == 45:
            cnt += 1

    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            SUM_b = 0
            for i in range(3):
                for j in range(3):
                    SUM_b += arr[i+k][j+l]
            if SUM_b == 45:
                cnt += 1

    if cnt == 27:
        print('#{} 1'.format(TC))
    else:
        print('#{} 0'.format(TC))
