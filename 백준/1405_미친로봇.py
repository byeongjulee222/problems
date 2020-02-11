import sys; sys.stdin = open('txt/1405_미친로봇.txt', 'r')

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def backtrack(x, y, move, prob):
    global ans, visit
    if move == N:
        ans += prob
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (nx, ny) in visit:
            visit.append((nx, ny))
            backtrack(nx, ny, move+1, prob*P[i])
            visit.pop()

N, p_e, p_w, p_s, p_n = map(int, input().split())
P = [p_e/100, p_w/100, p_s/100, p_n/100]
ans = 0
visit = [(0, 0)]
backtrack(0, 0, 0, 1)
print('{:.10f}'.format(ans))