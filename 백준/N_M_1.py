def perm(k):
    global M
    if k == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if visit[i]: continue
        visit[i] = 1
        arr.append(i)
        perm(k+1)
        visit[i] = 0
        arr.pop()

arr = []
N, M = map(int, input().split())
visit = [0] * (N+1)
perm(0)