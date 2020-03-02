import sys; sys.stdin = open('txt/14501_퇴사.txt', 'r')

for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    compare = [0] * N

    # i: 처음 시작일자 선택
    for i in range(N):
        # 그 날짜 + 그 날짜에 시작하는 일의 소요 기간
        if i + arr[i][0] <= N:
            compare[i] = arr[i][1]
            for j in range(i):
                # 날짜 범위 안에서
                if j + arr[j][0] <= i:
                    # i번까지 올 때 최대 = max(i번까지 올 때 최대 vs i번까지의 합)
                    compare[i] = max(compare[i], compare[j] + arr[i][1])
    print(max(compare))
