import sys; sys.stdin = open("txt/2115_honey.txt", "r")

T = int(input())
# for tc in range(1, T+1):
N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
