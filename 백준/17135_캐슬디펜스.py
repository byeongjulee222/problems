import sys; sys.stdin = open('txt/17135_캐슬디펜스.txt', 'r')
from itertools import combinations
from collections import deque
from copy import deepcopy

def Attack(enemy):
    global killed
    target = [(0, Max) for _ in range(3)]
    dist = [Max for _ in range(3)]

    while enemy:
        x, y = enemy.popleft()
        # archer의 3명
        for i in range(3):
            # archer의 행은 N으로 고정
            # archer와 적 거리 중 가장 작은 값 저장 (그 때의 적 좌표 저장)
            d = abs(N-x) + abs(archer_loc[i]-y)
            if dist[i] > d:
                dist[i] = d
                target[i] = (x, y)

            # 같은 거리에 있는 적이 여럿일 때, 가장 왼쪽의 적을 선택
            if dist[i] == d and y < target[i][1]:
                target[i] = (x, y)

    # 목표로 설정된 적 제거
    for i, (x, y) in enumerate(target):
        if Map[x][y]:
            if dist[i] <= D:
                Map[x][y] = 0
                killed += 1


for tc in range(1, int(input())+1):
    N, M, D = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    castle = [i for i in range(M)]
    ans = 0
    Max = 100000
    enemy = deque()

    for archer_loc in combinations(castle, 3):
        # print(archer_loc)
        #
        Map = deepcopy(arr)
        killed = 0
        while True:
            for i in range(N):
                for j in range(M):
                    if Map[i][j]:
                        enemy.append((i, j))

            if len(enemy) == 0: break

            Attack(enemy)

            # 적 밑으로 내리기
            Map = [[0] * M] + Map[:N-1]
        ans = max(ans, killed)
    print(ans)