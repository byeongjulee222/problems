import sys; sys.stdin = open('txt/2178_미로 탐색.txt', 'r')
import collections

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, cnt):
    global Min
    if x == N-1 and y == M-1:
        # print(x, y, cnt)
        Min = min(cnt, Min)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and arr[nx][ny] == 1:
            visit[nx][ny] = True
            # print(nx, ny, cnt)
            dfs(nx, ny, cnt+1)
            visit[nx][ny] = False

def bfs(x, y, cnt):
    global Min
    q = collections.deque()
    q.append((x, y, cnt))
    while q:
        x, y, cnt = q.popleft()
        if x == N-1 and y == M-1:
            Min = min(Min, cnt)
            break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and arr[nx][ny] == 1:
                visit[nx][ny] = True
                q.append((nx, ny, cnt+1))

    return Min



# for _ in range(int(input())):
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)
visit = [[False] * M for _ in range(N)]
# print(visit)
Min = N*M
# dfs(0, 0, 1)
# print(Min)

print(bfs(0, 0, 1))