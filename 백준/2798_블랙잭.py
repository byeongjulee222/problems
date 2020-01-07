import sys; sys.stdin = open('txt/2798_블랙잭.txt', 'r')
from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)
result = []
# print(list(combinations(arr, 3)))
for a in combinations(arr, 3):
    if sum(a) <= M:
        result.append(sum(a))

print(max(result))