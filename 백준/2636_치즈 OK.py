import sys; sys.stdin = open('txt/2636_치즈.txt', 'r')
from pprint import pprint
sys.setrecursionlimit(10000)

# 외부 공기인 경우 'o'로 바꾸는 작업
def dfs(a, b):
    visit[a][b] = True
    arr[a][b] = 'o'
    for l in range(4):
        na, nb = a+dx[l], b+dy[l]
        if 0 <= na < Row and 0 <= nb < Col:
            if (arr[na][nb] == 0 or arr[na][nb] == 'o') and not visit[na][nb]:
                dfs(na, nb)

# 주변에 외부 공기가 있으면 테두리 치즈('c')로 변경
def find(x, y):
    global cnt
    visit[x][y] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if arr[nx][ny] == 'o':
            arr[x][y] = 'c'
            return

Row, Col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Row)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []

time = 0
while True:

    one = 0
    for find_one in arr:
        one += find_one.count(1)
    result.append(one)
    # print(result)

    visit = [[False] * Col for _ in range(Row)]
    dfs(0, 0)

    # 모두 공기로 바뀌었을 때 종료
    cnt = 0
    for lst in arr:
        cnt += lst.count('o')
    if cnt == Row * Col: break

    # 공기와 맞닿은 치즈인지
    for i in range(Row):
        for j in range(Col):
            if arr[i][j] == 1:
                find(i, j)

    # 공기와 맞닿은 치즈인 경우
    for i in range(Row):
        for j in range(Col):
            if arr[i][j] == 'c':
                arr[i][j] = 'o'
    time += 1

print(time)
print(result[-2])