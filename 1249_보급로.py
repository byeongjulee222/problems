import sys; sys.stdin = open('txt/1249_보급로.txt', 'r')
# 탐색 방향을 오른쪽, 아래 먼저 --> 휴리스틱 최적화
# Main Algorithm : 메모이제이션
from collections import deque

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    visit = [[-1]* N for _ in range(N)]
    # print(visit)
    visit[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1: continue
        # 그 위치까지 작업한 양을 cnt로 저장
        cnt = visit[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 방문한 적이 없거나, 방문한 기록이 지금 진행 경로값보다 크다면 현재 경로값을 저장
                if visit[nx][ny] == -1 or cnt + arr[nx][ny] < visit[nx][ny]:
                    visit[nx][ny] = cnt + arr[nx][ny]
                    q.append((nx, ny))

    print('#{} {}'.format(tc, visit[N-1][N-1]))



# 우선순위 큐 사용 조건

# P 문제일 것
# 그래프에 cycle이 존재하지 않을 것
# 모든 정점을 거칠 필요가 없을 것
# 간선의 비용이 양수일 것
#




# NP가 뭔지 알아보기, 대표적인 문제 풀어보기




