import sys; sys.stdin = open("txt/2070.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr, b = map(int, input().split())
    c = ''
    if arr > b:
        c = '>'
    elif arr < b:
        c = '<'
    else:
        c = '='
    print('#{} {}'.format(tc, c))