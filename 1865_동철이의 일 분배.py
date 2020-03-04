import sys; sys.stdin = open('txt/1865_동철이의 일 분배.txt', 'r')

def distrib(row):
    global Max, res

    # 다 돌았으면 확률 계산
    if row == N:
        Max = max(Max, res)
        return

    # 이미 확률이 더 낮아진 경우, 더 진행할 필요없음
    if Max > res: return

    # row를 돌며 모든 경우의 col을 순회(순열)
    for col in range(N):
        # 방문한 곳이거나 + 확률 0이면 안감
        if check[col] or not arr[row][col]: continue
        check[col] = 1
        res *= arr[row][col]
        distrib(row+1)
        check[col] = 0
        res /= arr[row][col]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 확률로 처리해주는 과정
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100

    check = [0 for _ in range(N)]
    Max = 0
    res = 1
    distrib(0)
    print('#{} {:.6f}'.format(tc, Max*100))