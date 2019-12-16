import sys; sys.stdin = open('txt/15686_치킨배달.txt', 'r')
from itertools import combinations

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chicken, home = [], []

    # 배열에서 치킨집, 집 찾아서 각 리스트에 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i, j))
            elif arr[i][j] == 2:
                chicken.append((i, j))

    # 치킨집을 기준으로 조합 돌려서
    # 집을 기준으로
    # 집~치킨집 거리의 최솟값을 dist에 저장
    # dist의 최솟값 출력
    result = 100000
    for chick in combinations(chicken, M):
        # print(chick)
        dist = 0
        for home_x, home_y in home:
            Min = 100000
            for chicken_x, chicken_y in chick:
                Min = min(Min, abs(home_x-chicken_x)+abs(home_y-chicken_y))
            dist += Min
        result = min(result, dist)

    print(result)
    # break
