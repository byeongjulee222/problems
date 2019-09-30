def comb(k, n):
    if k == M:
        print(*choose)
        return

    for i in range(n, N):
        if visit[i]: continue
        visit[i] = 1
        choose.append(arr[i])
        comb(k+1, i+1)
        choose.pop()
        visit[i] = 0


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
choose = []
visit = [0] * N
comb(0, 0)