import sys; sys.stdin = open('txt/15683_감시.txt', 'r')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#     동 서 남  북
dir = [0,
       [[0], [1], [2], [3]],
       [[0, 1], [2, 3]],
       [[0, 3], [0, 2], [1, 2], [1, 3]],
       [[0, 1, 2], [0, 2, 3], [0, 1, 3], [1, 2, 3]],
       [[0, 1, 2, 3]]
       ]

def watch(x, y, lst, val):
    for d in lst:
        nx, ny = x+dx[d], y+dy[d]
        while 0<=nx<N and 0<=ny<M and arr[nx][ny] != 6:
            visit[nx][ny] += val
            nx += dx[d]
            ny += dy[d]

def backtrack(k, n):
    global Min
    if k == n:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0 and not visit[i][j]:
                    cnt += 1
        Min = min(Min, cnt)
    else:
        x, y, d = cctv[k]
        for lst in dir[d]:
            watch(x, y, lst, 1)
            backtrack(k+1, n)
            watch(x, y, lst, -1)


for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cctv = []
    for i in range(N):
        for j in range(M):
            if 0 < arr[i][j] < 6:
                cctv.append((i, j, arr[i][j]))
    # print(cctv)
    # break
    visit = [[0]*M for _ in range(N)]
    Min = N*M
    backtrack(0, len(cctv))
    print(Min)