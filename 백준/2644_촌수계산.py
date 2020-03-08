import sys; sys.stdin = open('txt/2644_촌수계산.txt', 'r')
import collections

def bfs(v):
    q = collections.deque()
    visit = [False]*(n+1)
    q.append(v)
    visit[v] = True
    level = 0
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            if v == end:
                return level
            for e in G[v]:
                if not(visit[e]):
                    visit[e] = True
                    q.append(e)
        level += 1
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

print(bfs(start))