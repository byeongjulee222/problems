import sys; sys.stdin = open('txt/17144_미세먼지 안녕!.txt', 'r')

def diffuse():
    moving_dust = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] >= 5:
                center_dust = arr[i][j] // 5
                for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        moving_dust[nx][ny] += center_dust
                        arr[i][j] -= center_dust
    for i in range(r):
        for j in range(c):
            arr[i][j] += moving_dust[i][j]

def purify():
    # 위쪽 회전(반시계 방향)
    for i in range(upper-2, -1, -1):
        arr[i+1][0] = arr[i][0]
    for i in range(c-1):
        arr[0][i] = arr[0][i+1]
    for i in range(upper):
        arr[i][c-1] = arr[i+1][c-1]
    for i in range(c-2, -1, -1):
        arr[upper][i+1] = arr[upper][i]
    # 정화
    arr[upper][1] = 0
    
    # 아래쪽(시계 방향) 
    for i in range(lower+1, r-1):
        arr[i][0] = arr[i+1][0]
    for i in range(c-1):
        arr[r-1][i] = arr[r-1][i+1]
    for i in range(r-2, lower-1, -1):
        arr[i+1][c-1] = arr[i][c-1]
    for i in range(c-2, -1, -1):
        arr[lower][i+1] = arr[lower][i]
    # 정화
    arr[lower][1] = 0


for _ in range(int(input())):
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
upper, lower = -1, 0

for i in range(r):
    if arr[i][0] == -1:
        upper2 = i-1
        lower2 = i
        if upper == -1:
            upper = i
        else:
            lower = i

for _ in range(t):
    diffuse()
    purify()
print(sum(map(sum, arr)) + 2)