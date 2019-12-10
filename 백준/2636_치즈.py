import sys; sys.stdin = open('txt/2636_치즈.txt', 'r')
from pprint import pprint

def dfs(a, b):
    visit[a][b] = True
    for l in range(4):
        na, nb = a+dx[l], b+dy[l]
        if arr[na][nb] == 0 and not visit[na][nb]:
            arr[na][nb] = 'outer'
            dfs(na, nb)


def find(x, y):
    global cnt
    visit[x][y] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if arr[nx][ny] == 0:
            cnt += 1

    if cnt > 0: return True

Row, Col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Row)]
# print(arr)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visit = [[False] * Col for _ in range(Row)]

dfs(0, 0)
print(arr)

for i in range(Row):
    for j in range(Col):
        cnt = 0
        if arr[i][j] == 1:
            if find(i, j) == True:
                arr[i][j] = 'c'

pprint(arr)
