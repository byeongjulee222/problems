import sys; sys.stdin = open('txt/14502_연구소.txt', 'r')
from itertools import combinations
import copy
import time
import pprint

now = time.time()

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
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False]*M for _ in range(N)]

    # 경우의 수 줄이기 ( 벽이거나 바이러스이면 벽을 세울 장소에서 제외 )
    row_col = [(i, j) for i in range(N) for j in range(M)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 or arr[i][j] == 2:
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

        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    dfs(i, j)

        cnt = 0
        # print(arr)
        for i in range(N):
            cnt += check_arr[i].count(0)

        if Max <= cnt:
            Max = cnt
    print(Max)
    # break

print(time.time()-now)