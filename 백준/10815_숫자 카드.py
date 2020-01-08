import sys; sys.stdin = open('txt/10815_숫자 카드.txt' ,'r')

N = int(input())
# 원 배열을 list말고 set으로 받으니까 통과
# list로 제출하면 시간초과
arr1 = set(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

for m in arr2:
    if m in arr1:
        print(1, end=' ')
    else:
        print(0, end=' ')
