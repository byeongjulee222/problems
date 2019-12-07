import sys; sys.stdin = open('txt/1948_날짜 계산기.txt', 'r')

result = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, int(input())+1):
    a, b, c, d = map(int, input().split())
    start = (a, b)
    end = (c, d)
    res = 0
    for i in range(a+1, c):
        res += result[i]

    if a < c:
        res += result[a] - b + 1
    res += d

    print('#{} {}'.format(tc, res))