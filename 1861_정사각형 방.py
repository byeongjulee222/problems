import sys; sys.stdin = open('txt/1861_정사각형 방.txt', 'r')
# sys.setrecursionlimit(100000)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    cnt += 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
            dfs(nx, ny)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Max = 2

    for i in range(N):
        for j in range(N):
            if arr[i][j] == N**2:
                x, y = i, j

    # x, y = 0, 0

    for i in range(N):
        for j in range(N):
            cnt = 0
            dfs(i, j)
            if Max < cnt:
                Max = cnt
                x, y = i, j
            elif Max == cnt and arr[x][y] >= arr[i][j]:
                x, y, = i, j

    print('#{} {} {}'.format(tc, arr[x][y], Max))
