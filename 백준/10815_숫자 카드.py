import sys; sys.stdin = open('txt/10815_숫자 카드.txt' ,'r')

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

result = []
for m in arr2:
    if m in arr1:
        result.append(1)
    else:
        result.append(0)

print(*result)
