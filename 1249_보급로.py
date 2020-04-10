import sys; sys.stdin = open('txt/1249_보급로.txt', 'r')
# 탐색 방향을 오른쪽, 아래 먼저 --> 휴리스틱 최적화
from collections import deque

dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visit = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visit[0][0] = 0

    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1: continue

        cnt = visit[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visit[nx][ny] == -1 or cnt + arr[nx][ny] < visit[nx][ny]:
                    visit[nx][ny] = cnt + arr[nx][ny]
                    q.append((nx, ny))

    print('#{} {}'.format(tc, visit[N-1][N-1]))