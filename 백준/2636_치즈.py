import sys; sys.stdin = open('txt/2636_치즈.txt', 'r')
from pprint import pprint

def dfs(a, b):
    if arr[a][b] == 0 and not visit[a][b]: arr[a][b] = 'o'
    visit[a][b] = True
    for l in range(4):
        na, nb = a+dx[l], b+dy[l]
        if 0 <= na < Row and 0 <= nb < Col:
            if arr[na][nb] == 0 and not visit[na][nb]:
                arr[na][nb] = 'o'
                dfs(na, nb)


def find(x, y):
    global cnt
    visit[x][y] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if arr[nx][ny] == 'o':
            cnt += 1

    if cnt > 0: return True

Row, Col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Row)]
# print(arr)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visit = [[False] * Col for _ in range(Row)]

cnt = 0
while True:
    for lst in arr:
        cnt += lst.count('o')
    if cnt == Row*Col: break

    for i in range(Row):
        for j in range(Col):
            if arr[i][j] == 'c':
                arr[i][j] = 'o'

    for i in range(Row):
        for j in range(Col):
            if arr[i][j] == 0:
                dfs(i, j)
                break
            break
    pprint(arr)

    for i in range(Row):
        for j in range(Col):
            cnt = 0
            if arr[i][j] == 1:
                if find(i, j) == True:
                    arr[i][j] = 'c'

    pprint(arr)


pprint(arr)
'''
def outskirt_dfs(x, y):
    arr[x][y] = -1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '0':
            outskirt_dfs(nx, ny)


def check(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == -1:
            arr[x][y] = 0


N, M = map(int, input().split())
arr = []
cheese = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(N):
    arr += [input().split()]
    for j in range(M):
        if arr[i][j] == '1':
            cheese += 1
time = 0
outskirt_dfs(0, 0)
remain = 0
while cheese:
    remain = cheese
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                check(i, j)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                outskirt_dfs(i, j)
                cheese -= 1
    time += 1
print(time)
print(remain)
'''