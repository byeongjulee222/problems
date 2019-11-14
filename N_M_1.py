def perm(k):
    global M
    if k == M:
        print(*order)
        return

    for i in range(1, N+1):
        if visit[i]: continue
        visit[i] = 1
        order.append(i)
        # print(order)
        perm(k+1)
        order.pop()
        # print(order)
        visit[i] = 0

order = []
N, M = map(int, input().split())
visit = [0] * (N+1)
perm(0)