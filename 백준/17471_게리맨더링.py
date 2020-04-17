import sys; sys.stdin = open('txt/17471_게리맨더링.txt', 'r')
from itertools import combinations

def dfs(start, group):
    visit[start] = True
    for way in G[start]:
        # 둘이 같은 그룹에 있는지 확인
        if way in group and not visit[way]:
            dfs(way, group)

for tc in range(int(input())):
    N = int(input())
    people = [0] + list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        G[i] = list(map(int, input().split()))[1:]
    # print(G)
    arr = list(range(1, N+1))
    Min = 0xffffff
    # 두 그룹으로 나누기
    # k: 첫 그룹에 몇 개를 넣을지
    for k in range(1, N//2+1):
        for comb in combinations(arr, k):
            A = list(comb)
            B = []
            for i in arr:
                if i not in A:
                    B.append(i)
            print(A, B)

            # 모두 방문했으면 모두 연결 가능한 상태이다.
            visit = [False for _ in range(N+1)]
            dfs(A[0], A)
            if len(A) != visit.count(True): continue

            visit = [False for _ in range(N+1)]
            dfs(B[0], B)
            if len(B) != visit.count(True): continue

            sum_A, sum_B = 0, 0
            for i in A:
                sum_A += people[i]
            for i in B:
                sum_B += people[i]
            Min = min(Min, abs(sum_A-sum_B))

    # 두 그룹으로 나눌 수 없다 == Min 값이 변하지 않았다
    print(-1 if Min == 0xffffff else Min)


'''
def dfs(v, group, visit):
    visit[v] = True
    for w in G[v]:
        if w in group and not visit[w]:
            dfs(w, group, visit)
            
            
        visit = [False] * (N+1)
        dfs(A[0], A, visit)
        if len(A) != visit.count(True): continue

for tc in range(1, int(input())+1):
    N = int(input())
    people = [0] + list(map(int, input().split()))
    G = [[]]
    for i in range(N):
        tmp = list(map(int, input().split()))[1:]
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

        print('A: ', A)
        print('B: ', B)
        break

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