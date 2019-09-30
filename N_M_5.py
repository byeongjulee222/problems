def perm(k, s):
    if k == M:
        print(*choose)
        return

    for i in range(N):
        if visit[i]: continue
        visit[i] = 1
        choose.append(arr[i])
        perm(k+1, s+1)
        choose.pop()
        visit[i] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
choose = []
visit = [0] * N
perm(0, 0)