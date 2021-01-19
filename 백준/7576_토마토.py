import sys; sys.stdin = open('txt/7576_토마토.txt', 'r')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(M, N):
    day = -1
    while Q:
        day += 1
        for _ in range(len(Q)):
            Row, Col = Q.popleft()
            for i in range(4):
                nrow, ncol = Row + dx[i], Col + dy[i]
                if 0 <= nrow < N and 0 <= ncol < M and Map[nrow][ncol] == 0:
                    Map[nrow][ncol] = Map[Row][Col] + 1
                    Q.append((nrow, ncol))

    for m in Map:
        if 0 in m:
            return -1
    return day


# for tc in range(int(input())):
M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            Q.append((i, j))
print(bfs(M, N))