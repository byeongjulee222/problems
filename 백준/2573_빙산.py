import sys; sys.stdin = open('txt/2573_빙산.txt', 'r')

from pprint import pprint
# 빙산 찾아서 주변에 0 개수 찾아서 저장 (cnt)
# 1년 지날 때마다 cnt만큼 숫자 감소 ( max(0, cnt) )
# 배열 돌면서 덩어리 개수 찾기
# 덩어리 개수가 2개 이상될 때 그만
# from collections import deque
# from copy import deepcopy
#
# import sys
# sys.setrecursionlimit(1000000)
# def bfs(a, b):
#     q = deque()
#     q.append((a, b))
#     visit[a][b] = True
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < Row and 0 <= ny < Col:
#                 if not visit[nx][ny] and arr[nx][ny] != 0:
#                     q.append((nx, ny))
#                     visit[nx][ny] = True
#
#
# def dfs(a, b):
#     visit[a][b] = True
#     for d in range(4):
#         nx, ny = a+dx[d], b+dy[d]
#         if 0 <= nx < Row and 0 <= ny < Col:
#             if not visit[nx][ny] and arr[nx][ny] != 0:
#                 dfs(nx, ny)
#                 # visit[nx][ny] = True
#     # return
#
#
# # 네 방향에 있는지 찾기
# def find(x, y):
#     for a in range(4):
#         nx, ny = x+dx[a], y+dy[a]
#         if 0 <= nx < Row and 0 <= ny < Col:
#             if arr[nx][ny] == 0:
#                 ocean_cnt[x][y] += 1
#     # return
#
# # for _ in range(int(input())):
# Row, Col = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(Row)]
# # print(arr)
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# year = 0
# num = 0
# while True:
#     if num >= 2: break
#     num = 0
#     # 바다와 접한 면 개수 세기
#     ocean_cnt = [[0]*Col for _ in range(Row)]
#     for i in range(1, Row-1):
#         for j in range(1, Col-1):
#             if arr[i][j] != 0:
#                 find(i, j)
#                 # arr[i][j] = max(arr[i][j], 0)
#     # pprint(arr)
#
#     # 녹이는 작업
#     for i in range(Row):
#         for j in range(Col):
#             arr[i][j] -= ocean_cnt[i][j]
#             if arr[i][j] < 0: arr[i][j] = 0
#
#     # 빙산 개수 세기
#     visit = [[False] * Col for _ in range(Row)]
#     for i in range(1, Row-1):
#         for j in range(1, Col-1):
#             if not visit[i][j] and arr[i][j] != 0:
#                 # visit[i][j] = True
#                 # dfs(i, j)
#                 bfs(i, j)
#                 num += 1
#     # print('num: ', num)
#     # pprint(arr)
#
#     year += 1
#
# print(year if num else 0)

# 2, 19


# 큐에 빙산 좌표 넣어놓고 뽑다가 더이상 못뽑을 때 그룹 수 += 1


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
            if arr[i][j] != 0 and visit[i][j] == 0:
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