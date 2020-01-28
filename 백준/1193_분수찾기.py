n = int(input())

cnt = 0
while n > 0:
    n -= cnt
    cnt += 1

n = cnt + n - 1

if cnt % 2: print('{}/{}'.format(n, cnt-n))
else: print('{}/{}'.format(cnt-n, n))