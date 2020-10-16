# import sys; sys.stdin = open("txt/bj_2667.txt", "r")
# # DFS (1)
# # result 리스트를 만들어서 단지 수 추가
# # len(result) 출력하고
# # result 를 오름차순 정렬한 후 print
#
# dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
#
# def dfs(x, y):
#     global cnt
#     # 방문했으면 그 지점은 0으로 변경
#     arr[x][y] = 0
#     visit[x][y] = True
#     for i in range(4):
#         nx, ny = x+dx[i], y+dy[i]
#         # 경계조건 + 방문조건 + 맵에서의 위치 값 == 1
#         if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and arr[nx][ny] == 1:
#             cnt += 1
#             dfs(nx, ny)
#     return cnt
#
# N = int(input())
# arr = [list(map(int, input())) for _ in range(N)]
# # print(arr)
#
# visit = [[False]*N for _ in range(N)]
# res = []
# # 1인 지점을 만났을 때 그 지점을 개수에 포함시켜야 하므로
# # cnt = 1로 시작한다.
# cnt = 1
# for i in range(N):
#     for j in range(N):
#         # 맵은 하나로 고정 되어있기 때문에
#         # not visit으로 끊어낼 수 있다
#         if arr[i][j] == 1 and not visit[i][j]:
#             dfs(i, j)
#             res.append(cnt)
#             cnt = 1
#
# # .sort()는 변경사항이 저장됨
# res.sort()
# print(len(res))
# for i in res:
#     print(i)




import sys; sys.stdin = open("txt/2667_단지 번호붙이기.txt")
from collections import deque


# def bfs(r, c):
#     global visit, cnt
#     visit[r][c] = True
#
#     q = deque()
#     q.append((r, c))
#     while q:
#         r, c = q.popleft()
#         dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         for i in range(4):
#             nr, nc = r + dir[i][0], c + dir[i][1]
#             if 0 <= nr < N and 0 <= nc < N:
#                 if not visit[nr][nc] and arr[nr][nc] == 1:
#                     q.append((nr, nc))
#                     cnt += 1
#                     visit[nr][nc] = True
#
#     return cnt
#
# res = []
# arr = []
# N = int(input())
# visit = [[False]*N for _ in range(N)]
# # print(visit)
# for row in range(N):
#     arr.append(list(map(int, input())))
# # print(arr)
#
# cnt = 1
# for i in range(N):
#     for j in range(N):
#         if not visit[i][j] and arr[i][j] == 1:
#             res.append(bfs(i, j))
#             cnt = 1
#
# print(len(res))
# res = sorted(res)
# for i in res:
#     print(i)



dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def dfs(x, y):
    global cnt
    arr[x][y] = 0
    visit[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and arr[nx][ny]:
            cnt += 1
            dfs(nx, ny)
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
res = []
visit = [[False] * N for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visit[i][j]:
            res.append(dfs(i, j))
            cnt = 1

res.sort()
print(len(res))
for i in res:
    print(i)





















