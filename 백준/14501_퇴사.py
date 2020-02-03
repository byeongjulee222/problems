import sys; sys.stdin = open('txt/14501_퇴사.txt', 'r')
'''
for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    dp = [0] * N

    for i in range(N):
        if i + arr[i][0] <= N:
            dp[i] = arr[i][1]
            for j in range(i):
                if j + arr[j][0] <= i:
                    dp[i] = max(dp[i], dp[j] + arr[i][1])

    print(max(dp))
'''
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # break
    compare = [0] * N

    for i in range(N):
        if i + arr[i][0] <= N:
            compare[i] = arr[i][1]
            for j in range(i):
                if j + arr[j][0] <= i:
                    compare[i] = max(compare[i], compare[j] + arr[i][1])
    print(max(compare))
