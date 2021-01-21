import sys; sys.stdin=open('txt/9372_상근이의 여행.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    # G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        # G[a].append(b)
        # G[b].append(a)
    print(N-1)

