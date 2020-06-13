import sys; sys.stdin = open("txt/2071.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print('#{} {:.0f}'.format(tc, sum(arr)/10))