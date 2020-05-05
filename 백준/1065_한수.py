import sys; sys.stdin = open('txt/1065_한수.txt', 'r')

def hansu(num):
    cnt = 0
    if num == 1000: cnt = 144
    elif num >= 100:
        cnt += 99
        for i in range(100, num+1):
            a = i // 100
            b = (i // 10) % 10
            c = i % 10
            if a - b == b - c:
                cnt += 1
    else:
        cnt = num

    return cnt

for _ in range(int(input())):
    N = int(input())
    print(hansu(N))
