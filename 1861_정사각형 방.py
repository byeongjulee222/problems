import sys; sys.stdin = open('txt/1861_정사각형 방.txt', 'r')
'''
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    cnt += 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
            dfs(nx, ny)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Max = 2

    for i in range(N):
        for j in range(N):
            if arr[i][j] == N**2:
                x, y = i, j

    for i in range(N):
        for j in range(N):
            cnt = 0
            dfs(i, j)
            if Max < cnt:
                Max = cnt
                x, y = i, j
            elif Max == cnt and arr[x][y] >= arr[i][j]:
                x, y, = i, j

    print('#{} {} {}'.format(tc, arr[x][y], Max))
'''

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 정답 후보들을 배열에 저장한다고 생각
    ans = [0 for _ in range(N ** 2)]

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                # 이동할 수 있으면 1을 저장
                if 0 <= nx < N and 0 <= ny < N and arr[i][j] + 1 == arr[nx][ny]:
                    ans[arr[i][j]] = 1
                    # 그 방향으로 이동할 수 있으면 다른 방향은 검색할 필요 없음.
                    # 배열안의 모든 값은 서로 다른 값이기 때문
                    break

    # 시작점을 출력하기 위해 뒤에서부터 탐색
    for i in range(N ** 2 - 1, -1, -1):
        # 이동할 수 있는 값이 연속된다면 값을 누적해간다
        if ans[i] and ans[i - 1]:
            ans[i - 1] += ans[i]

    # .index를 하면 해당하는 값 중 index값이 작은 것을 출력한다.
    print('#{} {} {}'.format(tc, ans.index(max(ans)), max(ans) + 1))