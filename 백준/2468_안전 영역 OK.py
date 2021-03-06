import sys; sys.stdin = open('txt/2468_안전 영역.txt', 'r')
from pprint import pprint
sys.setrecursionlimit(10000)

def dfs(x, y):
    visit[x][y] = True
    # 아래 배열을 돌 때 i, j를 사용했기 때문에
    # 다른 변수 k 를 사용하는 것이 안전하다
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] > height and not visit[nx][ny]:
                dfs(nx, ny)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 섬의 높이 범위내에서 판단하면됨
# 최소값, 최대값을 미리 찾아두고 범위를 좁히는데 사용
Max_h, Min_h = 0, 100
for i in range(N):
    for j in range(N):
        if Max_h <= arr[i][j]: Max_h = arr[i][j]
        if Min_h >= arr[i][j]: Min_h = arr[i][j]

# <<중요>> 모든 지역이 안전지역인 경우 그룹 수 : 1
Max = 1

# 높이의 최소값, 최대값 범위를 돌며 Max 뽑아냄
for height in range(Min_h, Max_h+1):
    cnt = 0
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if height < arr[i][j] and not visit[i][j]:
                cnt += 1
                dfs(i, j)

    if Max <= cnt:
        Max = cnt

print(Max)


''' (수지씨)
import sys; sys.setrecursionlimit(10000)
sys.stdin = open('txt/2468_안전 영역.txt', 'r')

def DFS(x, y, h):

    for direction in range(4):
        nx = x + DIR[direction][0]
        ny = y + DIR[direction][1]
        if 0 <= nx < size and 0 <= ny < size:
            if not visit[nx][ny] and area[nx][ny] > h:
                visit[nx][ny] = True
                DFS(nx, ny, h)


size = int(input())
area = [list(map(int, input().split())) for _ in range(size)]
DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
num = 0
max_height = 0

for i in area:
    max_height = max(max(i), max_height)

num = 1
for rain_height in range(1, max_height+1):
    visit = [[False] * size for _ in range(size)]
    chk = 0
    for r in range(size):
        for c in range(size):
            if area[r][c] > rain_height and not visit[r][c]:
                chk += 1
                DFS(r, c, rain_height)
    num = max(num, chk)
print(num)
'''