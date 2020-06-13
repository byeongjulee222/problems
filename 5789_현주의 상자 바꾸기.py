import sys; sys.stdin = open("txt/5789_change_box.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())

    arr = ['0' for _ in range(N)]

    for i in range(1, Q+1):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            arr[j] = str(i)
    print('#{} {}'.format(tc, ' '.join(arr)))