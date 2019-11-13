import sys; sys.stdin = open('txt/BJ_17471.txt', 'r')

def dfs(v, group, visit):
    visit[v] = True
    for w in G[v]:
        if w in group and not visit[w]:
            dfs(w, group, visit)


for tc in range(1, int(input())+1):
    N = int(input())
    people = [0] + list(map(int, input().split()))
    G = [[]]
    for i in range(N):
        tmp = list(map(int, input().split()))
        tmp.pop(0)
        G.append(tmp)

    ans = 1000
    for set in range(2, 1<<(N+1)):
        A, B = [], []
        Asum, Bsum = 0, 0
        for i in range(1, N+1):
            if set & (1<<i):
                A.append(i)
                Asum += people[i]
            else:
                B.append(i)
                Bsum += people[i]

        if len(A) == 0 or len(B) == 0: continue
        if abs(Asum - Bsum) >= ans: continue
        # print(A)
        # print(B)

        visit = [False] * (N+1)
        dfs(A[0], A, visit)
        if len(A) != visit.count(True): continue

        visit = [False] * (N+1)
        dfs(B[0], B, visit)
        if len(B) != visit.count(True): continue

        ans = min(ans, abs(Asum-Bsum))

    if ans == 1000: ans = -1
    print(ans)




'''
from collections import deque
from itertools import permutations

def bfs(a):
    visit = [False] * (N+1)
    q.append(a)

    while q:
        x = q.popleft()
        for w in G[x]:
            if not visit[w]:
                q.append(w)
                visit[w] = True

def subset(k):
    if k == N:
        town1 = A
        town2 = B
    else:
        A.append(towns[k])
        subset(k+1)
        A.pop()

        B.append(towns[k])
        subset(k+1)
        B.pop()


for tc in range(1, int(input())+1):
    N = int(input())
    towns = [i for i in range(1, N+1)]
    people = list(map(int, input().split()))
    q = deque()
    G = [[] for _ in range(N+1)]
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(1, arr[0]+1):
            G[i+1].append(arr[j])

    # print(G)
    A, B = [], []
    town1, town2 = [], []
    subset(0)
    print(town1, town2)
'''