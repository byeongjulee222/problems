import sys; sys.stdin = open('input_03.txt', 'r')


def backtrack(k, C, m): # k: 미네랄번호, C: 로봇의 에너지, m: 지금까지 채취한 미네랄의 양
    global ans
    if ans < m:
        ans = m
    if k == len(mineral):
        return

    #k 번 미네랄을 채취를 할 것인지
    if C >= mineral[k][0]:
        backtrack(k + 1, C - mineral[k][0], m + mineral[k][1])

    #k 번 미네랄 스킵
    backtrack(k + 1, C, m)


TC = int(input())
for tc in range(1, TC + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sx = sy = 0
    tmp = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                sx, sy = i, j
            elif arr[i][j]:
                tmp.append((i, j))
    mineral = []
    for x, y in tmp:
        mineral.append(((abs(sx - x) + abs(sy - y)) * 2, arr[x][y]))
    ans = 0

    backtrack(0, C, 0)
    print(ans)