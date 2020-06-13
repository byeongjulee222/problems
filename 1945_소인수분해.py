import sys; sys.stdin = open('txt/D2_1945_소인수분해.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = b = c = d = e = 0
    while N > 1:
        if not N % 2:
            arr += 1
            N //= 2
        if not N % 3:
            b += 1
            N //= 3
        if not N % 5:
            c += 1
            N //= 5
        if not N % 7:
            d += 1
            N //= 7
        if not N % 11:
            e += 1
            N //= 11

    print('#{} {} {} {} {} {}'.format(tc, arr, b, c, d, e))