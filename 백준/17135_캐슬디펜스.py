import sys; sys.stdin = open('txt/17135_캐슬디펜스.txt', 'r')
from itertools import combinations
from collections import deque
from copy import deepcopy

for tc in range(1, int(input())+1):
    N, M, D = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    castle = [i for i in range(N)]

    ans = 0
    Max = 0xfffffff
    enemy = deque()

    for archers in combinations(castle, 3):
        Map = deepcopy(arr)
        killed = 0
        while True:
            # 적 위치 저장
            for i in range(N):
                for j in range(M):
                    if Map[i][j]:
                        enemy.append((i, j))

            # 종료 조건(Map에 적이 없을 때)
            if len(enemy) == 0: break

            # 최소 거리에 있는 적을 찾기위해 Max 거리를 최대로 지정
            # target은 번호 순서대로 궁수 번호와 맞춰서 몇 번 궁수가 어떤 적(좌표)를 선택했는지 저장
            target = [(0, Max) for _ in range(3)]
            dist = [Max for _ in range(3)]

            # enemy(deque)에 적이 있는 경우 계속 진행
            while enemy:
                x, y = enemy.popleft()
                # 궁수 3명 반복
                for i in range(3):
                    # 궁수 행은 N으로 고정, 열은 archers[i](조합)
                    d = abs(N - x) + abs(archers[i] - y)
                    # 사정거리 안에 들어왔을 때
                    if dist[i] > d:
                        # 거리를 d로 정해두고
                        dist[i] = d
                        # i번째 궁수의 타겟(좌표)을 저장
                        target[i] = (x, y)

                    # 사정거리 안에 있는 적이 여럿일 경우 y가 작은 거을 타겟으로 선정
                    if dist[i] == d and y < target[i][1]:
                        target[i] = (x, y)

            # 궁수별로 타겟을 다 정한 후
            #
            for i, (x, y) in enumerate(target):
                if Map[x][y]:
                    if dist[i] <= D:
                        Map[x][y] = 0
                        killed += 1

            Map = [[0] * M] + Map[:N-1]
        ans = max(ans, killed)

    print(ans)