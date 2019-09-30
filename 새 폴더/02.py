import sys; sys.stdin = open('input_02.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(10)]
    robot =[]
    cookie = []
    for i in range(10):
        for j in range(10):
            if data[i][j] == 9 :
                robot.append((i, j))
            if data[i][j] in range(1, 7):
                cookie.append((i, j))

    D = [[0] * 6 for _ in range(6)] # D[i][j] -> i번 로봇과 j번 과자의 거리
    for i in range(6):
        for j in range(6):
            D[i][j] = abs(robot[i][0] - cookie[j][0]) + abs(robot[i][1] - cookie[j][1])
    ans = 0xfffffff
    visit = [0] * 6
    def backtrack(k, dist):
        global ans
        if dist >= ans: return
        if k == 6:
            ans = dist
        else:
            for i in range(6):
                if visit[i]: continue
                visit[i] = 1
                backtrack(k + 1, dist + D[k][i])
                visit[i] = 0

    backtrack(0, 0)

    print(ans)