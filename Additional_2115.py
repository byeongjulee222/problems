import sys; sys.stdin = open('txt/Additional_2115.txt', 'r')

def collect(honeys):
    Max = 0
    # 배열 내에서 길이 M 만큼의 부분집합을 구함.
    for x in range(1 << M):
        honey = []
        for y in range(M):
            if x & (1 << y):
                honey.append(honeys[y])
        # print(honey)

        if sum(honey) <= C:
            Sum = 0
            for e in honey:
                Sum += e * e

            if Max < Sum:
                Max = Sum

    return Max


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    worker1, worker2 = 0, 0

    # 행 반복
    for i in range(N):
        Maxs = set()
        # 열 반복(전체 길이 - 조사 범위 + 1)
        for j in range(N-M+1):
            Maxs.add(collect(arr[i][j:j+M]))
        # print(Maxs)
        max_mid = max(Maxs)
        # print(max_mid)

        # 새로 들어오는 값이 더 클 때,
        # 이전까지 중 가장 큰 값도 그대로 저장해서 가져감
        if worker1 < max_mid:
            worker1, worker2 = max_mid, worker1
        elif worker2 < max_mid:
            worker2 = max_mid

    print('#{} {}'.format(tc, worker1+worker2))