import sys; sys.stdin = open('txt/1260_DFS와 BFS.txt', 'r')
import collections
sys.setrecursionlimit(10000000)

def dfs(x):
    visit[x] = True
    for i in G[x]:
        if not visit[i]:
            visit[i] = True
            lst.append(i)
            dfs(i)

def bfs(x):
    q = collections.deque()
    q.append(x)
    visit[x] = True
    while q:
        a = q.popleft()
        lst.append(a)
        for k in G[a]:
            if not visit[k]:
                visit[k] = True
                q.append(k)



# for _ in range(int(input())):
N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    # print(a, b)
    G[a].append(b)
    G[b].append(a)
    # G[a].sort()
# print(G)
for i in range(N+1):
    G[i].sort()

# print(G)
visit = [False for _ in range(N + 1)]
# print(visit)
lst = [V]
dfs(V)
print(*lst)
visit = [False for _ in range(N + 1)]
lst = []
bfs(V)
print(*lst)
# ans.sort()
# break