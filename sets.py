# disjoint-sets

import sys; sys.stdin = open('txt/sets.txt', 'r')

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    p = [x for x in range(V + 1)] # 정점의 번호 1 ~ V
    print(p)
    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]

    ans = V
    for _ in range(E):
        u, v = map(int, input().split())
        arr = find_set(u); b = find_set(v)
        if arr == b: continue
        p[b] = arr
        ans -= 1
        print(p)
    # print(p)

    print('#{} {}'.format(tc, ans))


# MST_KRUSKAL

V, E = map(int, input().split())

Edge, MST = [], []
for _ in range(E):
    Edge.append(tuple(map(int, input().split())))

#================================
p = [0] * V
def init():
    for i in range(V):
        p[i] = i

def find(a):
    if p[a] == a: return a
    p[a] = find(p[a])
    return p[a]

#================================

Edge.sort(key=lambda x: x[2])
init()
cnt, cur = V - 1, 0
while cnt and cur <= V:
    u, v, w = Edge[cur]
    arr, b = find(u), find(v)
    if arr != b:
        p[arr] = b
        MST.append((u, v, w))
        cnt -= 1
    cur += 1

for edge in MST:
    print(edge)


# MST_PRIM

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

key = [0xfffff] * V      # 0 ~ V-1 (큰 값을 미리 넣어둠)
pi = [0] * V    # 0 => NULL(없다)
key[0] = 0      # key 초기값 0 (처음 선택한 node~node)

cnt = V
visit = [False] * V     # 트리에 포함된 정점들, 아닌 정점들 구분하기 위해서
while cnt:      # 정점의 수만큼 반복
    u = MIN = 0xffffff
    # key 값이 최소인 정점을 찾는다.
    for i in range(V):
        if not visit[i] and MIN > key[i]:
            u, MIN = i, key[i]
    visit[u] = True

    # u의 인접정점을 찾아서 key, pi를 변경
    for v, w in G[u]:
        if not visit[v] and w < key[v]:
            key[v], pi[v] = w, u

    cnt -= 1


for i in range(V):
    print(i, pi[i], key[i])
    

# 숙제
# 우선순위 Queue 사용해서 구현해보기

# BFS_shortest
from queue import Queue

def BFS(s, G):
    D = [0xffffff]*(V+1)
    D[s] = 0
    Q = Queue()
    Q.put(s)
    P = [i for i in range(V+1)]

    while Q:
        u = Q.get()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.put(v)

    print()


# DIJKSTRA_Array

def DIJKSTRA_ARRAY(s):

    D = [0xfffff] * (V + 1)
    P = [i for i in range(V + 1)]
    visit = [False] * (V + 1)
    D[s] = 0

    cnt = V
    while cnt:                              # 정점의 수 만큼 반복

        u, MIN = 0, 0xfffff                 # D[] 가 최소인 정점 찾기
        for i in range(1, V + 1):           # 무식하게 리스트에서 찾기
            if not visit[i] and D[i] < MIN:
                u, MIN = i, D[i]

        visit[u] = True

        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u

        cnt -= 1

    print(D[1: V + 1])
    print(P[1: V + 1])


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

DIJKSTRA_ARRAY(1)



# N 백
# 카드 뒤집기 -> 확률게임 (맞추면 10점, 틀리면 -750점) 40개중에 지뢰 1~2개
# 하노이(구슬)
# 공 무게
# 삼각형 모양 맞추기(순발력)
# 날씨 맞추기(예상)
# 색깔 좌우 맞추기
# 자음, 모음 / 홀수, 짝수 (맞는지 틀린지)
# 표정 맞추기
# 얼굴안에 막대 길이(짧은건지, 긴건지)