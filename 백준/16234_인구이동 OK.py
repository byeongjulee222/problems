import sys; sys.stdin = open('txt/16234_인구이동.txt', 'r')
# union 배열 만들어서 각 지역을 돌며 주변 국가와 비교해서
# L, R 조건을 만족하면 union에 넣기
# union에 이미 있으면 넣지 않기
# 배열 끝까지 돌면 union 안에 있는 국가들 인구 평균으로 변경
# 변경 후 day += 1
import collections

def bfs(map, a, b):
    q = collections.deque()
    union = set()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visit[x][y] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 경계조건 + 방문확인
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                # 국경선 open/close 조건
                if L <= abs(map[x][y] - map[nx][ny]) <= R:
                    # set.update(리스트) : 없는 항목만 set에 추가
                    union.update([(x, y), (nx, ny)])
                    q.append((nx, ny))
    return union


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(int(input())):
    N, L, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    day = 0
    while True:
        visit = [[False]*N for _ in range(N)]
        results = []
        for i in range(N):
            for j in range(N):
                if not visit[i][j]:
                    results.append(bfs(arr, i, j))

        # total = 0 을 여기에 두고 돌리는 실수를 해서 계속 틀림
        for result in results:
            total = 0
            if result:
                # 연합국 안에서 평균값 구하고
                for arr, b in result:
                    total += arr[arr][b]
                avg = total // len(result)
                
                # 국가별 인구를 평균값으로 변경
                for arr, b in result:
                    arr[arr][b] = avg

        # 인구이동 종료조건
        if len(results) == N*N: break

        day += 1
    print(day)