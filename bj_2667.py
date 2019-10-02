import sys; sys.stdin = open("txt/bj_2667.txt", "r")

def dfs(x, y):
    global cnt
    data[x][y] = 0
    visit[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
           if data[nx][ny] == 1:
                cnt += 1
                dfs(nx, ny)
    return cnt

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N = int(input())

data = [list(map(int, input())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
# n = 1
cnt = 1
result = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and not visit[i][j]:
            dfs(i, j)
            result.append(cnt)
            cnt = 1
            
result.sort()
print(len(result))
for i in result:
    print(i)