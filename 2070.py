import sys; sys.stdin = open("txt/2070.txt", "r")

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    c = ''
    if a > b:
        c = '>'
    elif a < b:
        c = '<'
    else:
        c = '='
    print('#{} {}'.format(tc, c))