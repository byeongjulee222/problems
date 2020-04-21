import sys; sys.stdin = open('txt/2573_빙산.txt', 'r')

import sys
from collections import deque
def bfs(x, y, visit):
    q = deque()
    q.append((x, y))
    melting_que = deque()
    visit[x][y] = True
    # q: 검사할 빙산
    # 빙산을 추가하면서 주변에 물이 있는지 함께 검사
    while q:
        x, y = q.popleft()
        melt_cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < Row and 0 <= ny < Col and not visit[nx][ny]:
                # 빙산의 높이가 있을 경우 검사할 빙산에 추가
                if arr[nx][ny] != 0:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                # 주변에 물이 있으면 cnt += 1
                else:
                    melt_cnt += 1

        # 녹는 빙산 추가
        if melt_cnt:
            melting_que.append((x, y, melt_cnt))

    # 빙산 녹이기
    while melting_que:
        # x좌표, y좌표, 녹는 양
        x, y, melt_cnt = melting_que.popleft()
        arr[x][y] = max(arr[x][y] - melt_cnt, 0)

    # return

Row, Col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Row)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

year = 0
while True:
    cnt = 0
    visit = [[False] * Col for _ in range(Row)]
    for i in range(1, Row-1):
        for j in range(1, Col-1):
            if arr[i][j] != 0 and not visit[i][j]:
                cnt += 1
                bfs(i, j, visit)


    # 빙산의 갯수가 0이거나 2이상일 경우 반복문 종료
    if cnt == 0:
        year = 0
        break
    if cnt >= 2:
        break

    # 다 돌았는데 안끝났으면 year += 1
    year += 1

print(year)