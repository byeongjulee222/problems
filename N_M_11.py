def perm(k, s):
    if k == M:
        result.add(tuple(choose))
        return

    for i in range(len(arr)):
        choose.append(arr[i])
        perm(k+1, i+1)
        choose.pop()




N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
# print(arr)
choose = []
result = set()
perm(0, 0)
final = sorted(list(result))
for i in final:
    print(*i)