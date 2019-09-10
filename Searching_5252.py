import sys; sys.stdin = open("txt/Searching_5252.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = [input() for _ in range(N)]
    M_list = [input() for _ in range(M)]

    result = [i for i in N_list if i in M_list]
    print('#{} {}'.format(tc, len(result)))