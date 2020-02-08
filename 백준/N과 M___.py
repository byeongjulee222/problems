def comb(k, s):
    if k == M:
        print(*arr)
        return
    else:
        for i in range(s, N):
            arr.append(i+1)
            comb(k+1, i+1)
            arr.pop()

N, M = map(int, input().split())
arr = []
arr1 = []
comb(0, 0)

visit = [0 for _ in range(N+1)]

def perm(k, s):
    if k == s:
        print(*arr)
        return
    else:
        for i in range(1, N+1):
            if not visit[i]:
                arr1.append(i)
                visit[i] = 1
                perm(k+1, s)
                visit[i] = 0
                arr.pop()
perm(0, M)