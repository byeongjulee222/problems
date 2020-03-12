import sys; sys.stdin=open('txt/1953_탈주범 검거.txt', 'r')
import collections

def move(r, c, t):
    global cnt
    Q = collections.deque()
    Q.append((r, c, t))
    visit[r][c] = True
    while Q:
        rr, cc, tt = Q.popleft()
        # 제한 시간 안에서만 돌도록
        if tt < L:
            # 현재 위치에서의 파이프의 방향
            for a, b in pipe[arr[rr][cc]]:
                # 경계조건
                if 0 <= rr+a < N and 0 <= cc+b < M:
                    # 탐색하는 위치에 파이프가 없으면 컨티뉴
                    if not arr[rr+a][cc+b]: continue
                    # 탐색하는 위치의 파이프 모양을 보고 이동할 수 있는지 판단
                    if not visit[rr+a][cc+b] and (-1 * a, -1 * b) in pipe[arr[rr+a][cc+b]]:
                        cnt += 1
                        visit[rr+a][cc+b] = True
                        Q.append((rr+a, cc+b, tt+1))

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 파이프별로 이동할 수 있는 방향을 저장
    pipe = {
        1: [(0, -1), (0, 1), (-1, 0), (1, 0)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (0, 1)],
        4: [(-1, 0), (0, 1)],
        5: [(1, 0), (0, 1)],
        6: [(1, 0), (0, -1)],
        7: [(-1, 0), (0, -1)]
    }

    visit = [[False]*M for _ in range(N)]
    cnt = 1
    move(R, C, 1)
    print(cnt)