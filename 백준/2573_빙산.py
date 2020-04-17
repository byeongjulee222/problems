import sys; sys.stdin = open('txt/2573_빙산.txt', 'r')
from pprint import pprint
# 빙산 찾아서 주변에 0 개수 찾아서 저장 (cnt)
# 1년 지날 때마다 cnt만큼 숫자 감소 ( max(0, cnt) )
# 배열 돌면서 덩어리 개수 찾기
# 덩어리 개수가 2개 이상될 때 그만
from collections import deque

import sys
sys.setrecursionlimit(1000000)
def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visit[x][y] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < Row and 0 <= ny < Col:
                if not visit[nx][ny] and arr[nx][ny] != 0:
                    q.append((nx, ny))


def dfs(a, b):
    visit[a][b] = True
    for d in range(4):
        nx, ny = a+dx[d], b+dy[d]
        if 0 <= nx < Row and 0 <= ny < Col:
            if not visit[nx][ny] and arr[nx][ny] != 0:
                dfs(nx, ny)
    # return


# 네 방향에 있는지 찾기
def find(x, y):
    for a in range(4):
        nx, ny = x+dx[a], y+dy[a]
        if 0 <= nx < Row and 0 <= ny < Col:
            if arr[nx][ny] == 0:
                arr[x][y] -= 1
                if arr[x][y] == 0: break
    # return

Row, Col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Row)]
# print(arr)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
year = 0
num = 0
while True:
    if num >= 2: break
    num = 0
    # visit = [[False] * Col for _ in range(Row)]
    for i in range(1, Row-1):
        for j in range(1, Col-1):
            if arr[i][j] != 0:
                find(i, j)
                # arr[i][j] = max(arr[i][j], 0)
    # pprint(arr)

    visit = [[False] * Col for _ in range(Row)]
    for i in range(1, Row-1):
        for j in range(1, Col-1):
            if not visit[i][j] and arr[i][j] != 0:
                # dfs(i, j)
                bfs(i, j)
                num += 1
    # print('num: ', num)
    # pprint(arr)

    year += 1

print(year if num else 0)