import sys; sys.stdin = open('txt/17135_캐슬디펜스.txt', 'r')
from itertools import combinations
from collections import deque
from copy import deepcopy

for tc in range(1, int(input())+1):
    N, M, D = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    castle = [i for i in range(M)]

    ans = 0
    Max = 0xffffff
    # 조합의 경우 모두 확인
    for archers in combinations(castle, 3):
        # 적을 큐(스택)에 담아서 하나씩 꺼내며 처리
        # 경우마다 킬 수는 0으로 초기화
        # 경우마다 Map을 원래의 arr로 deepcopy
        enemy = deque()
        killed = 0
        Map = deepcopy(arr)
        # 종료조건 만족할 때까지 반복
        while True:
            # Map에 0이 아닌 값이 있으면 적
            for i in range(N):
                for j in range(M):
                    if Map[i][j]: enemy.append((i, j))
            # 적이 없으면 종료
            if not len(enemy): break
            # 적을 타겟으로 선정할지 판단하기 위해(가까운 적 선택하기 위해 첫 조건은 큰 값)
            # 그 때의 거리값도 저장해서 거리가 같은 적이 있을 때 왼쪽 적을 선택함
            target = [(0, Max) for _ in range(3)]
            dist = [Max for _ in range(3)]

            # 적을 모두 판단하여 처리할 때까지 진행
            while enemy:
                x, y = enemy.popleft()
                # 궁수 3명이므로 3번 반복
                for i in range(3):
                    # 궁수와 적 거리값을 미리 변수화해둠
                    d = abs(N-x) + abs(archers[i] - y)
                    # 사정거리 내에 적이 들어왔을 때 타겟으로 선정(좌표 저장)
                    if d < dist[i]:
                        dist[i] = d
                        target[i] = (x, y)
                    # 사정거리가 같을 때, 왼쪽편에 있는 적으로 타겟 변경
                    if dist[i] == d and y < target[i][1]:
                        target[i] = (x, y)

            for i, (x, y) in enumerate(target):
                # Map에 적이 있고, 그 적이 사정거리 안에 있는지 다시 확인
                if Map[x][y] and dist[i] <= D:
                    # Map에 값을 0으로 바꾸고 kill 수 증가
                    Map[x][y] = 0
                    killed += 1
            # 밑으로 한칸 내림
            Map = [[0]*M] + Map[:N-1]
        ans = max(ans, killed)
    print(ans)