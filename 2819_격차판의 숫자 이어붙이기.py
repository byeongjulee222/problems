import sys; sys.stdin = open('txt/2819_격차판의 숫자 이어붙이기.txt', 'r')
# tc 1 : 23

for tc in range(1, int(input())):
    arr = [list(map(int, input().split())) for _ in range(4)]
