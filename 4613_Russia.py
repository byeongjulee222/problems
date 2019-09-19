import sys; sys.stdin = open("txt/4613_Russia.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    counts = []
    for flags in arr:
        print(flags.count('W'), flags.count('B'), flags.count('R'))
        counts.append(flags.count('B'))

    b_row = counts.index(max(counts))

    cnt = M - arr[b_row].count('B')
    # print(cnt)
    for i in range(b_row):
        cnt += arr[i].count('B')
        cnt += arr[i].count('R')

    # B 라인 다 바꾸고나서 그 다음 행에서 B보다 R의 수가 많으면 그때부터 R로 변경
    i = b_row
    while arr[i].count('B') >= arr[i].count('W'):
        cnt += arr[i].count('W') + arr[i].count('R')
        i += 1

    for j in range(i+1, N):
        cnt += arr[j].count('B')
        cnt += arr[j].count('W')

    print(cnt)