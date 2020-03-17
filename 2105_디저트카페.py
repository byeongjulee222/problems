import sys; sys.stdin = open('txt/2105_디저트카페.txt', 'r')

dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
def find(x, y, cnt, check):
    global Max
    if cnt == 4: return

    nx, ny = x+dir[cnt][0], y+dir[cnt][1]
    if 0 <= nx < N and 0 <= ny < N:
        if nx == i and ny == j and Max <= len(check):
            Max = len(check)
            return

        if cafes[nx][ny] not in check:
            check.append(cafes[nx][ny])
            find(nx, ny, cnt, check)
            find(nx, ny, cnt+1, check)
            check.pop()


for tc in range(1, int(input())+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    Max = -1
    for i in range(N):
        for j in range(N):
            check = []
            find(i, j, 0, [cafes[i][j]])

    print('#{} {}'.format(tc, Max))