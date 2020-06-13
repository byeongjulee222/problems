import sys; sys.stdin = open("txt/2072.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 0
    for i in arr:
        if i % 2:
            result += i
    print('#{} {}'.format(tc, result))