import sys; sys.stdin = open('txt/17135_캐슬디펜스.txt', 'r')

#

for tc in range(1, int(input())+1):
    N, M, D = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
