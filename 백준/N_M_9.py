def perm(k, s):
    if k == M:
        result.add(tuple(choose))
        return

    for i in range(N):
        if visit[i]: continue
        visit[i] = 1
        choose.append(arr[i])
        perm(k+1, i+1)
        choose.pop()
        visit[i] = 0


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
choose = []
visit = [0] * N
result = set()
perm(0, 0)
final = sorted(list(result))
for i in final:
    print(*i)