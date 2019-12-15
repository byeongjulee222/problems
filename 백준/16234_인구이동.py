import sys; sys.stdin = open('txt/16234_인구이동.txt', 'r')
# union 배열 만들어서 각 지역을 돌며 주변 국가와 비교해서
# L, R 조건을 만족하면 union에 넣기
# union에 이미 있으면 넣지 않기
# 배열 끝까지 돌면 union 안에 있는 국가들 인구 평균으로 변경
# 변경 후 day += 1
from copy import deepcopy
from collections import deque
def bfs(maps, a, b, visited):
    union = set()
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visit[x][y] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if L <= abs(arr[x][y]-arr[nx][ny]) <= R:
                    print(x, y, nx, ny, abs(arr[x][y]-arr[nx][ny]))
                    union.add((x, y))
                    q.append((nx, ny))
                    visit[nx][ny] = True
    return union


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

day = 0
while True:
    prev_arr = deepcopy(arr)
    visit = [[False] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if visit[i][j]
            bfs(i, j)

    total = 0
    if union:
        for a, b in union:
            total += arr[a][b]
        avg = total // len(union)
        print(union)
        print(avg)

        for a, b in union:
            arr[a][b] = avg

    if len(union) == N*N: break

print(day)



'''
def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visit[x][y] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if L <= abs(arr[x][y]-arr[nx][ny]) <= R:
                    print(x, y, nx, ny, abs(arr[x][y]-arr[nx][ny]))
                    union.add((x, y))
                    q.append((nx, ny))
                    visit[nx][ny] = True
    return


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

day = 0
while True:
    day += 1
    union = set()
    for i in range(N):
        for j in range(N):
            visit = [[False] * N for _ in range(N)]
            bfs(i, j)
    print('union: ', union)

    total = 0
    if union:
        for a, b in union:
            total += arr[a][b]
        avg = total // len(union)
        print(union)
        print(avg)

        for a, b in union:
            arr[a][b] = avg

    if len(union) == N*N: break

print(day)
'''

