import sys; sys.stdin = open("txt/Searching_5188.txt", "r")

def dfs(x, y):
    global result, final
    visit[x][y] = True
    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        if nx == N-1 and ny == N-1:
            result += arr[nx][ny]
            final.append(result)
        elif 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == False:
            result += arr[nx][ny]
            visit[nx][ny]
            dfs(nx, ny)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx, dy = [1, 0], [0, 1]
    visit = [[False]*N for _ in range(N)]

    final = []
    result = arr[0][0]
    dfs(0, 0)
    print(final)