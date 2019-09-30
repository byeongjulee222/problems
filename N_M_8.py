def comb(k, s):
    if k == M:
        print(*choose)
        return

    for i in range(s, N):
        choose.append(arr[i])
        comb(k+1, i)
        choose.pop()



N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
choose = []
comb(0, 0)