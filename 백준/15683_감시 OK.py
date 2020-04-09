import sys; sys.stdin = open('txt/15683_감시.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dir = [0,
       [[0], [1], [2], [3]],
       [[0, 1], [2, 3]],
       [[0, 3], [0, 2], [1, 3], [1, 2]],
       [[0, 1, 2], [0, 2, 3], [0, 1, 3], [1, 2, 3]],
       [[0, 1, 2, 3]]
       ]

def watch(x, y, lst, val):
    for d in lst:
        nx, ny = x+dx[d], y+dy[d]
        # 경계조건 + 벽이 아닌 조건
        while 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 6:
            visit[nx][ny] += val
            # 그 방향으로 계속 진행
            nx, ny = nx+dx[d], ny+dy[d]


def backtrack(k, s):
    global Min
    if k == s:
        cnt = 0
        for i in range(N):
            for j in range(M):
                # watch가 끝난 후 그 자리가 0이고, 방문한 적 없는 경우에만 count
                if not visit[i][j] and arr[i][j] == 0:
                    cnt += 1
        Min = min(Min, cnt)
    else:
        # 카메라 위치와 카메라 번호 가져옴
        x, y, d = cctv[k]
        # 카메라 종류에 따라 볼 수 있는 방향 모두 체크
        for lst in dir[d]:
            # 감시 가능한 곳이면 +1
            watch(x, y, lst, 1)
            backtrack(k+1, s)
            # 탐색 끝났으면 돌아오면서 숫자 빼줌
            watch(x, y, lst, -1)

for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 카메라 종류 리스트에 담아둠
    cctv = []
    for i in range(N):
        for j in range(M):
            if 0 < arr[i][j] < 6: cctv.append((i, j, arr[i][j]))

    # 한 번이라도 지나갔으면 0보다 크게됨
    Min = 0xfffff
    visit = [[0]*M for _ in range(N)]
    backtrack(0, len(cctv))
    print(Min)