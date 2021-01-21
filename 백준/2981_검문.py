import sys; sys.stdin=open('txt/2981_검문.txt', 'r')
from math import gcd

# def gcd(a, b):
#     while b:
#         a, b = b, a%b
#     return a

numbers = list()
N = int(input())
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
Min = numbers.pop(0)

for i in range(N-1):
    numbers[i] -= Min

gcd_n = numbers[0]
for i in range(N-1):
    gcd_n = gcd(gcd_n, numbers[i])

for div in range(2, gcd_n+1):
    if gcd_n % div == 0:
        print(div, end=' ')




''' 시간초과
ans = list()
for div in range(2, Min):
    flag = [False for _ in range(N)]
    last = Min % div
    for num in range(N):
        if numbers[num] % div == last:
            flag[num] = True
    if flag.count(True) == N:
        ans.append(div)
print(*ans)
'''