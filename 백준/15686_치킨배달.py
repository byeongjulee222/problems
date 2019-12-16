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


    ans = 100000
    for chick in combinations(chicken, M):
        # print(chick)
        s = 0
        for hx, hy in home:
            d = 100000
            for cx, cy in chick:
                d = min(d, abs(hx-cx)+abs(hy-cy))
            s += d
        ans = min(ans, s)

    print(ans)
    # break
