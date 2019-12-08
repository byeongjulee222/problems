N, M = map(int, input().split())
choose = []
def comb(k, s):
    if k == M:
        print(*choose)
        return

    for i in range(s, N):
        choose.append(i+1)
        comb(k+1, i+1)
        choose.pop()

comb(0, 0)