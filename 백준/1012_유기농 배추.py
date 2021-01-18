import sys; sys.stdin=open('txt/1012_유기농 배추.txt', 'r')
from pprint import pprint
# 추가해야 recursion error 패스
from sys import setrecursionlimit
setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(row, col):
    visit[row][col] = True
    for i in range(4):
        nrow, ncol = row+dy[i], col+dx[i]
        if 0 <= nrow < N and 0 <= ncol < M:
            if (row, col) in baechoo and not visit[nrow][ncol]:
                dfs(nrow, ncol)


for _ in range(int(input())):
    for tc in range(int(input())):
        M, N, K = map(int, input().split())
        baechoo = []
        visit = [[False for _ in range(M)] for _ in range(N)]
        cnt = 0
        for k in range(K):
            col, row = map(int, input().split())
            baechoo.append((row, col))
        for row, col in baechoo:
            if not visit[row][col]:
                cnt += 1
                dfs(row, col)
        print(cnt)