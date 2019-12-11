import sys; sys.stdin = open('txt/17822_원판돌리기.txt', 'r')

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for round in range(T):
    xi, di, ki = map(int, input().split())
# print(arr)
