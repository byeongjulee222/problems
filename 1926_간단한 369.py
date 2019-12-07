import sys; sys.stdin = open('txt/1926_간단한 369.txt', 'r')

arr = list(str(i) for i in range(1, int(input())+1))
# print(arr)

res = []
for i in arr:
    if '3' in i or '6' in i or '9' in i:
        res.append('-' * (i.count('3')+i.count('6')+i.count('9')))
    else:
        res.append(i)

print(*res)