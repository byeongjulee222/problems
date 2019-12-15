import sys; sys.stdin = open('txt/2589_보물섬.txt', 'r')
# 각 자리별 bfs 해서 그 자리에서 가장 먼 거리 저장
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    check[x][y] = True
    dist = 0
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if check[nx][ny] != True and arr[nx][ny] == 'L':
                    q.append((nx, ny, d+1))
                    check[nx][ny] = True
                    dist = max(dist, d+1)
    return dist

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# print(arr)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            check = [[False] * M for _ in range(N)]
            ans = max(ans, bfs(i, j))

print(ans)