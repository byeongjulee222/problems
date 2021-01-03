import sys; sys.stdin = open('txt/7575_바이러스.txt', 'r')


N, K = map(int, input().split())
M = int(input())

for i in range(N):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
    