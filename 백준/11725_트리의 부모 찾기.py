import sys; sys.stdin=open('txt/11725_트리의 부모 찾기.txt', 'r')
from collections import deque

for tc in range(int(input())):
    N = int(input())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    Q = deque()
    Q.append(1)
    ans = dict()
    check = [False for _ in range(N+1)]

    while Q:
        parent = Q.popleft()
        for i in G[parent]:
            if not check[i]:
                ans[i] = parent
                Q.append(i)
                check[i] = True

    for i in range(2, N+1):
        print(ans[i])