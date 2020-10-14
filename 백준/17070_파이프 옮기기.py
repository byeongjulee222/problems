# 답 : 1, 3, 0, 13

import sys; sys.stdin = open('txt/17070_파이프 옮기기.txt', 'r')


def pipe():
    pass


for _ in range(int(input())):
    N = int(input())
    Map = []
    for _ in range(N):
        Map.append(list(map(int,input().split())))
    print(Map)