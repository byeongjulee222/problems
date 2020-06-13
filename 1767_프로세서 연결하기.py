import sys; sys.stdin = open('SW_프로세서 연결하기.txt', 'r')
# 프로세서 연결하기
# 테두리 만들어놓고(&apos;e&apos;)
# 네 방향 탐색해서 e와 인접해있으면 연결되어 있다고 표시 후 continue

# 풀이
# 모두가 연결되지 않을 수 있다.
# 코어가 연결된 경우 / 연결되지 않은 경우
# 상 하 좌 우 네 방향중에 하나
# ---> 연결X, 상하좌우 : 총 다섯가지 경우

'''
N = 7


def backtrack(k):  # 함수 호출의 depth, 지금 고려할 코어의 번호
    if k == N:
        # 연결된 개수가 이전의 것보다 많으면
        #     코어개수, 길이 저장
        pass
    else:
        # k번을 연결하는 경우
        for i in range(4):
            # 상, 하, 좌, 우 중에 한 방향으로 연결
            backtrack(k + 1)

        # k번을 연결하지 않는 경우
        backtrack(k + 1)

'''

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def isConnect(k, dir):
    x, y = core[k]
    while True:
        x, y = x + dx[dir], y + dy[dir]
        if x < 0 or x == N or y < 0 or y == N: break
        if B[x][y]: return False
    return True


def setLine(k, dir, val):
    x, y = core[k]
    x, y = x + dx[dir], y + dy[dir]
    ret = 0
    while 0 <= x < N and 0 <= y < N:
        B[x][y] = val
        ret += 1
        x, y = x + dx[dir], y + dy[dir]
    return ret


def backtrack(k, n, cur):
    global cnt, minLen
    if k == ncore:
        if n > cnt:
            cnt, minLen = n, cur
        if n == cnt and cur < minLen:
            minLen = cur
        return

    # 코어 연결하기
    for i in range(4):
        if isConnect(k, i):
            ret = setLine(k, i, 2)
            backtrack(k + 1, n + 1, cur + ret)
            setLine(k, i, 0)

    # 연결하지 않기
    backtrack(k + 1, n, cur)


# -------------------------------------------
for tc in range(1, int(input()) + 1):
    N = int(input())
    B, core = [], []

    for i in range(N):
        arr = list(map(int, input().split()))
        B.append(arr)
        if 0 < i < (N - 1):
            for j in range(1, N - 1):
                if arr[j]: core.append((i, j))

    cnt, minLen = 0, 0xffffffff
    ncore = len(core)

    backtrack(0, 0, 0)
    print('# {} {}'.format(tc, minLen))