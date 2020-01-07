import sys; sys.stdin = open('txt/14501_퇴사.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    print(arr)
    break