import sys; sys.stdin=open('txt/1978_소수 찾기.txt', 'r')

# prime_num = [True for _ in range(1001)]
# for i in range(2, 1001):


N = int(input())
numbers = list(map(int, input().split()))
ans = 0

for num in numbers:
    cnt = 0
    for div in range(2, num+1):
        if not num % div:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)