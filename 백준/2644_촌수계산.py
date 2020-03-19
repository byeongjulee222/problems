import sys; sys.stdin = open('txt/2644_촌수계산.txt', 'r')
import collections

def bfs(v):
    global level
    visit[v] = True
    Q.append(v)
    while Q:
        for _ in range(len(Q)):
            a = Q.popleft()
            if a == end: return level
            for w in people[a]:
                if not visit[w]:
                    visit[w] = True
                    Q.append(w)
        level += 1
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
people = [[] for _ in range(n+1)]
for _ in range(m):
    arr, b = map(int, input().split())
    people[arr].append(b)
    people[b].append(arr)
print(people)

visit = [False for _ in range(n+1)]
Q = collections.deque()
level = 0

print(bfs(start))