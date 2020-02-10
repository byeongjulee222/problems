import sys; sys.stdin = open('txt/1405_미친로봇.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, move, prob):
    global ans, visit
    if move == N:
        if len(set(visit)) == N+1:
            ans += prob
        return

    for a in range(4):
        nx, ny = x+dx[a], y+dy[a]
        # 방문한 곳이 아니면 한 번 더 전진
        # 그 방향으로의 확률도 곱해준다
        if (nx, ny) not in visit:
            visit.append((nx, ny))
            dfs(nx, ny, move+1, prob*p[a])
            visit.pop()

N, p_e, p_w, p_s, p_n = map(int, input().split())
p = [p_e/100, p_w/100, p_s/100, p_n/100]
ans = 0
visit = [(0, 0)]
dfs(0, 0, 0, 1)
print('{:.10f}'.format(ans))