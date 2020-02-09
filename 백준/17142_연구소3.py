from copy import deepcopy
from itertools import combinations
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(virus, Map):
    # res에 최대시간 저장
    res = 0
    while Q:
        xx, yy, dist = Q.popleft()
        visit[xx][yy] = True
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and Map[nx][ny] != 1:
                visit[nx][ny] = True
                if Map[nx][ny] == 0:
                    Map[nx][ny] = 2
                    res = dist + 1
                Q.append((nx, ny, dist + 1))

    # 맵에 0이 있으면(다 퍼뜨리지 못한 경우)
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 0:
                return -1
    return res

for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0xfffff
    place = []

    # 바이러스 퍼뜨리는 것을 시작할 수 있는 위치 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                place.append((i, j, 0))

    # 각 경우별로 체크 실행
    for virus in combinations(place, M):
        Map = deepcopy(arr)
        visit = [[False] * N for _ in range(N)]
        Q = deque(virus)
        result = bfs(virus, Map)

        if result < ans and result != -1:
            ans = result

    if ans == 0xfffff:
        print(-1)
    else:
        print(ans)