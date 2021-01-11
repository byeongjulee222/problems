import sys; sys.stdin = open('txt/2580_스도쿠.txt', 'r')
# 백트래킹 문제

arr = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]

def find_cadidates(i ,j):
    numbers = [i for i in range(1, 10)]

    # 가로, 세로 확인
    for k in range(9):
        if arr[i][k] in numbers:
            numbers.remove(arr[i][k])
        if arr[k][j] in numbers:
            numbers.remove(arr[k][j])

    # 3x3 칸 확인
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if arr[p][q] in numbers:
                numbers.remove(arr[p][q])

    return numbers

flag = False
def dfs(n):
    global flag

    if flag: return
    elif n == len(zeros):
        for i in arr:
            print(*i)
        flag = True
        return
    else:
        (i, j) = zeros[n]
        candidates = find_cadidates(i, j)

        # 들어갈 수 있는 숫자 하나씩 넣어보기
        for num in candidates:
            arr[i][j] = num
            dfs(n+1)
            arr[i][j] = 0

dfs(0)