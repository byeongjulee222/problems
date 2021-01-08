import sys; sys.stdin = open('txt/1541_잃어버린 괄호.txt', 'r')

lst = input().split('-')

ans = 0
for i in lst[0].split('+'):
    ans += int(i)


for i in lst[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)