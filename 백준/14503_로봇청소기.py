import sys;sys.stdin = open('txt/14503_로봇청소기.txt', 'r')

# 방향에 대한 규칙을
# 왼쪽으로 돌면 (현재방향 + 3) % 4
# 뒤쪽 확인할 때 (현재방향 + 2) % 4

# 입력 : 북 동 남 서 = 0 1 2 3

def clean(x, y, d):
    d = (d+3) % 4
    nx, ny = x+dir[d[0]], y+dir[d[1]]
    if arr[nx][ny] == 0:
        pass


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                clean(i, j, d)
































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