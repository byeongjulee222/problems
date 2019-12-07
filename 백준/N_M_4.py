def comb(k, s):
    if len(choose) == 2:
        print(*choose)
        return

    for i in range(s, N):
        choose.append(arr[i])
        comb(k+1, i)
        choose.pop()

N, M = map(int, input().split())
arr = list(range(1, N+1))
choose = []
comb(0, 0)