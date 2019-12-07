def perm(k, n):
    global M
    if k == M:
        print(*order)
        return

    for i in range(1, N+1):
        if visit[i]: continue
        order.append(i)
        perm(k+1, n)
        order.pop()

order = []
N, M = map(int, input().split())
visit = [0] * (N+1)
perm(0, N)