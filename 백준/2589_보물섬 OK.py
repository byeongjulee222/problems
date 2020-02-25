import sys; sys.stdin = open('txt/2589_보물섬.txt', 'r')
import collections

# 모든 'L'을 돌면서 각 자리에서 가장 멀리 있는 'L'까지의 거리를 구하고
# 그 거리들 중 최대값을 구하는 문제
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

# bfs로 풀어야 이동 거리를 알 수 있음
def bfs(x, y, d):
    Max = 0
    visit[x][y] = True
    Q = collections.deque()
    Q.append((x, y, d))
    while Q:
        x, y, d = Q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and arr[nx][ny] == 'L':
                # pop해 온 자리에서 이동할 수 있으면 d+1
                Q.append((nx, ny, d+1))
                visit[nx][ny] = True
        Max = max(Max, d)
    return Max

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        # 모든 'L'을 돌며 탐색
        if arr[i][j] == 'L':
            visit = [[False]*M for _ in range(N)]
            ans = max(bfs(i, j, 0), ans)


print(ans)




















'''
# 각 자리별 bfs 해서 그 자리에서 갈 수 있는 가장 먼 거리(dist) return
from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, b, 0))
    visit[a][b] = True
    dist = 0
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny] and arr[nx][ny] == 'L':
                    q.append((nx, ny, d+1))
                    visit[nx][ny] = True
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
            visit = [[False]*M for _ in range(N)]
            ans = max(ans, bfs(i, j))
            # print(i, j)
            # print(ans)
print(ans)
'''