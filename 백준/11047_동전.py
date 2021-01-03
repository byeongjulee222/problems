import sys; sys.stdin = open('txt/11047_동전.txt', 'r')

for tc in range(int(input())):
    N, K = map(int, input().split())
    # print(N, K)

    cases = list()
    for i in range(N):
        case = int(input())
        cases.append(case)
        if case < K: stop = i
    cases = cases[:stop+1]
    # print(cases)

    cnt = 0
    for j in reversed(cases):
        if j <= K:
            cnt += K//j
            K -= K//j * j
            # print(K)
        if K == 0: break
    # print('cnt', cnt)
    print(cnt)