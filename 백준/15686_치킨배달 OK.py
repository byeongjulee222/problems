import sys; sys.stdin = open('txt/15686_치킨배달.txt', 'r')
from itertools import combinations
'''
def comb(k, s):
    if k == M:
        return

    for i in range(s, N):
        chicken_list.append(i)
        comb(k + 1, i + 1)
        chicken_list.pop()
'''

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chicken, chicken_list, home = [], [], []

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










# 15686.py 치킨배달
# 치킨거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨거리 : 모든 집의 치킨거리 합
for tc in range(1, int(input())+1):
    def getSet(k, s):
        if k == M:
            global MIN
            sumDist = 0
            for j in range(H):
                tmp = 100 # i번 치킨집 - j번 집 치킨거리
                for i in selected:
                    tmp = min(tmp, dist[i][j])
                sumDist += tmp
                if sumDist >= MIN: return
            MIN = sumDist
            return

        for idx in range(s, C):
            selected[k] = idx
            getSet(k + 1, idx + 1)
    #----------------------------------------------------------
    chicken = []    # 치킨집위 위치 저장
    home = []       # 집의 위치 저장
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1: home.append((i, j))
            elif board[i][j] == 2: chicken.append((i, j))

    C, H = len(chicken), len(home)
    print('chicken: ', chicken)

    # 치킨집 ~ 집 거리 미리 저장
    dist = [[] for _ in range(C)] # 치킨집(행) - 집(열) 거리 리스트
    print(dist)
    for i in range(C):
        x1, y1 = chicken[i]
        for j in range(H):
            x2, y2 = home[j]
            dist[i].append(abs(x1 - x2) + abs(y1 - y2))

    MIN = 0xffffff
    selected = [0] * M  # 선택된 치킨집
    getSet(0, 0)
    print('dist: ', dist)
    print('selelcted: ', selected)
    print(MIN)