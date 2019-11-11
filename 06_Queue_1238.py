import sys; sys.stdin = open("txt/Queue_1238.txt", "r")

from collections import deque

def bfs(a):
    q.append(a)

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visit[w]:
                dist[w] = dist[v] + 1
                visit[w] = True
                q.append(w)

    Max = 0
    for i in range(1, 101):
        if not dist[i]: continue
        if dist[i] >= dist[Max]: Max = i

    return Max


for tc in range(1, 11):
    L, S = map(int, input().split())
    q = deque()
    G = [[] for _ in range(101)]
    dist = [0] * 101
    visit = [False] * 101
    arr = list(map(int, input().split()))

    for i in range(0, L, 2):
        G[arr[i]].append(arr[i+1])

    print('#{} {}'.format(tc, bfs(S)))













# from collections import deque
#
# def bfs(a):
#     dist = [0] * 101
#     visit = [False] * 101
#
#     q.append(a)
#     while q:
#         v = q.popleft()
#         for w in G[v]:
#             if not visit[w]:
#                 dist[w] = dist[v] + 1
#                 visit[w] = True
#                 q.append(w)
#
#     # 크기 비교
#     Max = dist[a]
#     for i in range(1, 101):
#         if not visit[i]: continue
#         if dist[Max] <= dist[i]: Max = i
#
#     return Max
#
#
#
# for tc in range(1, 11):
#     L, S = map(int, input().split())
#     q = deque()
#     G = [[] for _ in range(101)]
#     arr = list(map(int, input().split()))
#
#     for i in range(0, L, 2):
#         G[arr[i]].append(arr[i+1])
#
#     print('#{} {}'.format(tc, bfs(S)))