import sys; sys.stdin = open('txt/2606_바이러스.txt', 'r')

def dfs(x):
    visit[x] = True
    res = 1
    for w in arr[x]:
        if visit[w]: continue
        res += dfs(w)
    return res

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)

visit = [False for _ in range(N+1)]

print(dfs(1) -1)