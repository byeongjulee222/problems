import sys; sys.stdin = open('txt/3079_입국심사.txt', 'r')

for _ in range(int(input())):
    N, M = map(int, input().split())
    inspect = []
    for _ in range(N):
        inspect.append(int(input()))

    print(inspect)