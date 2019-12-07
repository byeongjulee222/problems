def perm(k, s):
    if k == M:
        print(*choose)
        return

    for i in range(N):
        choose.append(arr[i])
        perm(k+1, s)
        choose.pop()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
choose = []
perm(0, 0)