import sys; sys.stdin = open('txt/1959.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(N, M)
    Max = 0
    for j in range(abs(N-M)+1):
        Sum = 0
        if N < M:
            for i in range(min(N, M)):
                Sum += A[i] * B[i+j]
            if Sum > Max:
                Max = Sum
        else:
            for i in range(min(N, M)):
                Sum += A[i+j] * B[i]
            if Sum > Max:
                Max = Sum

    print('#{} {}'.format(tc, Max))