import sys; sys.stdin = open('txt/16234_인구이동.txt', 'r')
# union 배열 만들어서 각 지역을 돌며 주변 국가와 비교해서
# L, R 조건을 만족하면 union에 넣기
# union에 이미 있으면 넣지 않기
# 배열 끝까지 돌면 union 안에 있는 국가들 인구 평균으로 변경
# 변경 후 day += 1

from collections import deque

def bfs(maps, a, b):
    q = deque()
    union = set()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visit[x][y] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visit[nx][ny]:
                if L <= abs(maps[x][y]-maps[nx][ny]) <= R:
                    union.update([(x, y), (nx, ny)])
                    q.append((nx, ny))
                    visit[nx][ny] = True
    return union

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

day = 0
while True:
    visit = [[False] * N for _ in range(N)]
    results = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if not visit[i][j]:
                results.append(bfs(arr, i, j))

    # total = 0 을 여기에 두고 돌리는 실수를 해서 계속 틀림
    for result in results:
        total = 0
        if result:
            for a, b in result:
                total += arr[a][b]
            avg = total // len(result)

            for a, b in result:
                arr[a][b] = avg

    if len(results) == N*N: break
    day += 1

print(day)