import sys; sys.stdin = open('txt/2798_블랙잭.txt', 'r')
from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)
result = []
# print(list(combinations(arr, 3)))
for arr in combinations(arr, 3):
    if sum(arr) <= M:
        result.append(sum(arr))

print(max(result))