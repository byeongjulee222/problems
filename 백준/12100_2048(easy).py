import sys; sys.stdin = open('txt/12100_2048.txt', 'r')

from collections import deque
from copy import deepcopy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
q = deque()

def add(i, j):
    # 값이 있으면 큐에 넣고 그 자리는 0
    if arr[i][j]:
        q.append(arr[i][j])
        arr[i][j] = 0

def merge(i, j, di, dj):
    while q:
        x = q.popleft()
        # 비교하는 칸이 0이면 그 자리에 넣는다(자리 채우기)
        if arr[i][j] == 0:
            arr[i][j] = x
        # 값이 같으면 합침
        elif arr[i][j] == x:
            arr[i][j] *= 2
            i, j = i+di, j+dj
        # 값이 다르면 그대로 넣고 i, j만 수정
        else:
            arr[i+di][j+dj] = x
            i, j = i+di, j+dj


def move(i):
    # 위로 밈
    if i == 0:
        for j in range(N):
            for i in range(N):
                add(i, j)
            # di += 1로 위에서 아래로가면서 검사
            merge(0, j, 1, 0)
    # 아래로 밈
    elif i == 1:
        for j in range(N):
            for i in range(N-1, -1, -1):
                add(i, j)
            merge(N-1, j, -1, 0)
    # 왼쪽으로 밈
    elif i == 2:
        for i in range(N):
            for j in range(N):
                add(i, j)
            merge(i, 0, 0, 1)
    # 오른쪽으로 밈
    else:
        for i in range(N):
            for j in range(N-1, -1, -1):
                add(i, j)
            merge(i, N-1, 0, -1)



def solve(cnt):
    global ans, arr
    if cnt == 5:
        for i in range(N):
            ans = max(ans, max(arr[i]))
            # print(arr)
        return

    box = deepcopy(arr)
    for i in range(4):
        move(i)
        solve(cnt+1)
        arr = deepcopy(box)

solve(0)
print(ans)