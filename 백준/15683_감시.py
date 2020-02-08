import sys; sys.stdin = open('txt/15683_감시.txt', 'r')

#  동, 서, 남, 북 순서
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# cctv가 보는 방향을 cctv 종류에 따라 저장
dir = [0,
       [[0], [1], [2], [3]],
       [[0, 1], [2, 3]],
       [[0, 2], [0, 3], [1, 2], [1, 3]],
       [[0, 1, 2], [0, 2, 3], [0, 1, 3], [1, 2, 3]],
       [[0, 1, 2, 3]]
       ]

def watch(x, y, lst, val):
    # cctv가 바라보는 방향 경우 중 한 방향씩 체크
    for d in lst:
        nx, ny = x+dx[d], y+dy[d]
        # 경계 조건 + 벽을 만났을 경우 제외 조건
        while 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 6:
            visit[nx][ny] += val
            # 체크하는 방향으로 쭉 체크
            nx, ny = nx+dx[d], ny+dy[d]

def backtrack(k, n):
    global Min
    # cctv 개수만큼 반복(종료 조건)
    if k == n:
        cnt = 0
        for i in range(N):
            for j in range(M):
                # watch가 끝난 후 그 자리가 0이고, 방문한 적 없는 경우에만 count
                if arr[i][j] == 0 and not visit[i][j]:
                    cnt += 1
        Min = min(Min, cnt)
    else:
        # cctv 좌표와 종류 불러옴
        x, y, d = cctv[k]
        # cctv 종류별 바라보는 방향 반복
        for lst in dir[d]:
            watch(x, y, lst, 1)
            backtrack(k+1, n)
            # 끝까지 내려갔을 때 되돌아오기(backtracking)
            watch(x, y, lst, -1)

for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # cctv 값 저장(좌표값, 종류 번호)
    cctv = []
    for i in range(N):
        for j in range(M):
            if 0 < arr[i][j] < 6: cctv.append((i, j, arr[i][j]))

    Min = 0xffffff
    visit = [[0]*M for _ in range(N)]
    # cctv 리스트 원소 개수만큼 반복
    backtrack(0, len(cctv))
    print(Min)