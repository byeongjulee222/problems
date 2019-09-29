def comb(k, s):
    if k == M:
        print(*choose)
        return

    for i in range(s, N):
        choose.append(arr[i])
        comb(k+1, i+1)
        choose.pop()

N, M = map(int, input().split())
arr = list(range(1, N+1))
choose = []
comb(0, 0)