import sys; sys.stdin = open("txt/4613_Russia.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    comb = [(i, j) for i in range(1, N-1) for j in range(i+1, N)]
    # print(comb)
    Min = 99999

    for i in range(len(comb)):
        cnt = 0
        for j in range(comb[i][0]):
            cnt += M - arr[j].count('W')

        for j in range(comb[i][0], comb[i][1]):
            cnt += M - arr[j].count('B')

        for j in range(comb[i][1], N):
            cnt += M - arr[j].count('R')

        Min = min(Min, cnt)

    print('#{} {}'.format(tc, Min))