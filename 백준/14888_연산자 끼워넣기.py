import sys; sys.stdin = open('txt/14888_연산자 끼워넣기.txt', 'r')
from itertools import permutations
from collections import deque
from copy import deepcopy

def cal(i, res, plus, minus, times, div):
    global Max, Min
    if i == N:
        Max = max(Max, res)
        Min = min(Min, res)
        return

    else:
        if plus:
            cal(i+1, res+arr[i], plus-1, minus, times, div)
        if minus:
            cal(i+1, res-arr[i], plus, minus-1, times, div)
        if times:
            cal(i+1, res*arr[i], plus, minus, times-1, div)
        if div:
            cal(i+1, int(res/arr[i]), plus, minus, times, div-1)


# + - * /
for _ in range(int(input())):
N = int(input())
arr = list(map(int, input().split()))
# print(arr)
# break
plus, minus, times, div = map(int, input().split())

Max = 0
Min = 999999999
cal(1, arr[0], plus, minus, times, div)
print(Max)
print(Min)



    '''
    pmtd = ['+', '-', '*', '//']
    pmtd_lst = list(map(int, input().split()))

    lst = []
    for i in range(4):
        for _ in range(pmtd_lst[i]):
            lst.append(pmtd[i])

    # print(lst)
    perm = list(permutations(lst, len(lst)))

    Min = 999999
    Max = -999999
    for i in perm:
        result = arr[0]
        for j in range(len(i)):
            if i[j] == '+':
                result += arr[j+1]
            elif i[j] == '-':
                result -= arr[j+1]
            elif i[j] == '*':
                result *= arr[j+1]
            elif i[j] == '//':
                result = int(result/arr[j+1])
        Min = min(Min, result)
        Max = max(Max, result)

    print(Max)
    print(Min)
    '''