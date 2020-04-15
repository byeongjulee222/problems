import sys; sys.stdin = open('txt/1949_등산로 조성.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def move(x, y, cnt, chance):
    global Max
    visit[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
            # 높이가 낮아서 진행할 수 있으면 dfs 전진
            if arr[nx][ny] < arr[x][y]:
                move(nx, ny, cnt+1, chance)

            # 전진할 수 없을 때 기회가 남아있으면
            elif chance:
                for cut in range(1, K+1):
                    if arr[nx][ny] - cut < arr[x][y]:
                        arr[nx][ny] -= cut
                        move(nx, ny, cnt+1, 0)
                        # dfs 끝까지 다 가봤으면 원상복구
                        arr[nx][ny] += cut
                        break

    if Max < cnt: Max = cnt
    visit[x][y] = False

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    high = 0
    for i in range(N):
        high = max(high, max(arr[i]))
    # print(Max)

    cand = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == high:
                cand.append((i, j))
    # print(cand)
    visit = [[False]*N for _ in range(N)]
    chance = 1
    Max = 0
    for x, y in cand:
        move(x, y, 1, 1)

    print('#{} {}'.format(tc, Max))
    # break