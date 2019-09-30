import sys; sys.stdin = open('input_01.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 99999
    H = 0
    for r in range(N):
        for c in range(N):
            for h in range(1, 6):
                cost = 0
                for i in range(N):
                    cost += abs(arr[r][i] - h)
                    cost += abs(arr[i][c] - h)
                cost -= abs(arr[r][c] - h)

                if Min > cost:
                    Min, H = cost, h

                elif Min == cost:
                    H = min(H, h)

    print(Min, H)