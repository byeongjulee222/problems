import sys;sys.stdin = open('txt/14503_로봇청소기.txt', 'r')

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d, cnt):
    visit[x][y] = True
    # 왼쪽 방향으로 돌아야하니
    # dx, dy 작성한 것의 반대 방향으로 돌아야 함
    for i in range(-3, 1):
        ndir = (d-i)%4
        nx = x+dx[ndir]
        ny = y+dy[ndir]
        # 진행하는 방향이 청소할 수 있는 곳이면
        # 이동해서 청소 (위치, 방향 바꾸고 cnt+1)
        # 경계 체크
        if 0 <= nx < N and 0 <= ny < M:
            # 벽 or 방문한 곳 체크
            if not arr[nx][ny] and not visit[nx][ny]:
                clean(nx, ny, ndir, cnt+1)
                return

    # 네 방향 다 체크하며 clean이 모두 동작한 후
    # 처음 보던 방향의 반대(-) 방향 체크
    # 비어있다면 후진
    if not arr[x-dx[d]][y-dy[d]]:
        clean(x-dx[d], y-dy[d], d, cnt)
        
    # 벽이라면 끝낸다
    else:
        print(cnt)
        return


for _ in range(int(input())):
    N, M = map(int, input().split())
    loc_x, loc_y, head = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False]*M for _ in range(N)]
    # 현재 위치 청소하기 때문에 cnt = 1 부터 시작
    clean(loc_x, loc_y, head, 1)





'''
for _ in range(int(input())):
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a[x][y] = 2
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

    def solve(x, y, d, ans):
        while True:
            c = False
            for k in range(4):
                nd = (d+3)%4
                nx, ny = x+dx[nd], y+dy[nd]
                d = nd
                if not a[nx][ny]:
                    a[nx][ny] = 2
                    ans += 1
                    x, y = nx, ny
                    c = True
                    break
            if not c:
                if a[x-dx[d]][y-dy[d]] == 1:
                    return ans
                else:
                    x, y = x-dx[d], y-dy[d]

    print(solve(x, y, d, 1))

'''
'''
동균

import sys; sys.stdin = open('r.txt', 'r')
from pprint import pprint
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
N, M = map(int, input().split())
robot = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

def clean_r(r, c, d, cnt):
    visit[r][c] = 1
    for i in range(-3, 1):
        ndir = (d-i) % 4
        nr = r + dr[ndir]
        nc = c + dc[ndir]
        if 0<=nr<N and 0<=nc<M:
            if arr[nr][nc] or visit[nr][nc]: continue
            clean_r(nr, nc, ndir, cnt+1)
            return
    if arr[r-dr[d]][c-dc[d]]:
        print(cnt)
        return
    else:
        clean_r(r - dr[d], c - dc[d], d, cnt)

clean_r(robot[0], robot[1], robot[2], 1) # x, y, dir
'''
'''
박진희

# 14503.py 로봇청소기
def getCnt(x, y, d):
    visit = [[False] * M for _ in range(N)]
    ret = 1
    visit[x][y] = True
    while True:
        for _ in range(4):
            dx, dy = xy[dir[d]] # 왼쪽 방향
            nx, ny = x + dx, y + dy
            if not board[nx][ny] and not visit[nx][ny]: # 2-a
                d = dir[d]
                x, y = nx, ny
                ret += 1 # 1. 청소
                visit[x][y] = True
                break
            else: # 2-b
                d = dir[d]
        else: # 2-c,d
            op = d #  반대방향
            for _ in range(2):
                op = dir[op]
            nx, ny = x + xy[op][0], y + xy[op][1]
            if not board[nx][ny]: x, y = nx, ny # 2-c
            else: break # 2-d
    return ret

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # d:방향 - 0북, 1동, 2남, 3서
board = [list(map(int, input().split())) for _ in range(N)]
dir = { 0: 3, 3: 2, 2: 1, 1: 0 }
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
print(getCnt(r, c, d))
'''

'''
김준영

N, M = map(int, input().split())
x, y, d = map(int ,input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)] # 청소한 곳 표시
# 북(0), 동(1), 남(2), 서(3)
direction = [3, 0, 1, 2]    # 왼쪽 방향
di = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}
back = [(1, 0), (0, -1), (-1, 0), (0, 1)]
cnt = 0
result = 0
flag = 0
while True: # x, y = 현재 위치
    if board[x][y] == 0 and not visit[x][y]: # 청소하기
        visit[x][y] = True
        result += 1
        continue
    if cnt == 4:
        dx, dy = back[d]
        tx = x + dx
        ty = y + dy
        if -1 < tx < N and -1 < ty < M and board[tx][ty] == 0:
            x = tx
            y = ty
            cnt = 0
            flag = 1
            continue
        else:
            break
    dx, dy = di[d]
    tx = x + dx
    ty = y + dy
    if -1 < tx < N and -1 < ty < M and board[tx][ty] == 0 and not visit[tx][ty]:
        x = tx
        y = ty
        d = direction[d]
        cnt = 0
    else:
        d = direction[d]
        cnt += 1
print(result)
'''