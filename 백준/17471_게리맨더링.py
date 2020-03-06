import sys; sys.stdin = open('txt/17471_게리맨더링.txt', 'r')
from itertools import combinations

for _ in range(int(input())):
    N = int(input())
    people = [0] + list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        G[i] = list(map(int, input().split()))[1:]
    # print(G)

    arr = list(range(1, N+1))
    for comb in combinations(arr, N//2):













'''
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