import sys; sys.stdin = open('txt/14502_연구소.txt', 'r')
import itertools
import collections
import copy
from pprint import pprint
# bfs : 964 ms
# dfs : 1340 ms

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    Q = collections.deque()
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and copied_arr[nx][ny] == 0:
                copied_arr[nx][ny] = 2
                visit[nx][ny] = True
                Q.append((nx, ny))

def dfs(x, y):
    visit[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and copied_arr[nx][ny] == 0:
            copied_arr[nx][ny] = 2
            visit[nx][ny] = True
            dfs(nx, ny)


for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 바이러스와 빈칸의 좌표 저장
    virus = []
    place = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virus.append((i, j))
            elif arr[i][j] == 0:
                place.append((i, j))

    Max = 0
    # 빈 칸들 중 3개 뽑는 조합
    for comb in itertools.combinations(place, 3):
        # 각 경우마다 맵 새로해줌
        copied_arr = copy.deepcopy(arr)
        visit = [[False] * M for _ in range(N)]
        # 벽 세우기
        for x, y in comb:
            copied_arr[x][y] = 1

        # 바이러스 퍼뜨리기
        for x, y in virus:
            bfs(x, y)
            # dfs(x, y)

        # 바이러스 안퍼진 곳 개수 카운트
        cnt = 0
        for i in range(N):
            for j in range(M):
                if copied_arr[i][j] == 0:
                    cnt += 1

        Max = max(Max, cnt)

    print(Max)

'''
from itertools import combinations
import copy
import time
import pprint


# 벽을 3개 세울 수 있다.
# 벽 3개를 세운 후 바이러스 활동 시작
# 활동이 끝난 후 0의 개수 count (최대값 구하기)
# 벽 3개를 두는 모든 경우를 구해야하나? (조합)
# 런타임에러 발생 --> 제출할 때 import 빼먹음 (해결)

def dfs(x, y):
    visit[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visit[nx][ny] and check_arr[nx][ny] == 0:
                visit[nx][ny] = True
                check_arr[nx][ny] = 2
                dfs(nx, ny)
                visit[nx][ny] = False

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    now = time.time()
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False]*M for _ in range(N)]

    # 경우의 수 줄이기 ( 벽이거나 바이러스이면 벽을 세울 장소에서 제외 )
    virus = []
    row_col = [(i, j) for i in range(N) for j in range(M)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                row_col.pop(row_col.index((i, j)))
            if arr[i][j] == 2:
                virus.append((i, j))
                row_col.pop(row_col.index((i, j)))


    # 벽 3개 세우는 경우의 수 만들기
    comb = list(combinations(row_col, 3))

    Max = 0
    for lst in comb:
        # 경우마다 원래의 배열 상태와 비교해야 하므로 deepcopy 사용
        # deepcopy : 복합객체를 새롭게 생성하고 그 안의 내용까지 재귀적으로 새롭게 생성
        #            --> 어느 한 쪽을 수정하더라도 다른 쪽에 영향 X
        check_arr = copy.deepcopy(arr)
        # print(lst)
        for l in lst:
            check_arr[l[0]][l[1]] = 1

        for i, j in virus:
            dfs(i, j)
        # for i in range(N):
        #     for j in range(M):
        #         if arr[i][j] == 2:
        #             dfs(i, j)

        cnt = 0
        # print(arr)
        for i in range(N):
            cnt += check_arr[i].count(0)

        if Max <= cnt:
            Max = cnt
    print(Max)

    print(time.time()-now)
'''