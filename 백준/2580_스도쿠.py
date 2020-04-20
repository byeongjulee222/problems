import sys; sys.stdin = open('txt/2580_스도쿠.txt', 'r')
# 백트래킹 문제

def backtrack():
    pass

numbers = [i for i in range(1, 10)]

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

for i in range(9):
    if arr[i].count(0) == 1:
        for j in sorted(arr[i]):
            if j == numbers[j-1]: pass
