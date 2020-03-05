import sys; sys.stdin = open('txt/2819_격자판의 숫자 이어붙이기.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def find(x, y, word):
    if len(word) == 7:
        nums.add(word)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            find(nx, ny, word+str(arr[nx][ny]))

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    nums = set()

    for i in range(4):
        for j in range(4):
            find(i, j, str(arr[i][j]))

    print('#{} {}'.format(tc, len(nums)))