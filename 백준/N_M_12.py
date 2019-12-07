def comb(k, s):
    if k == M:
        result.add(tuple(choose))
        return

    for i in range(s, len(arr)):
        # if visit[i]: continue
        # visit[i] = 1
        choose.append(arr[i])
        comb(k+1, i)
        choose.pop()
        # visit[i] = 0



N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
# print(arr)
choose = []
visit = [0] * N
result = set()
comb(0, 0)
final = sorted(list(result))
for i in final:
    print(*i)