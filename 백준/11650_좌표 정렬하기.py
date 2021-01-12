import sys; sys.stdin = open('txt/11650_좌표 정렬하기.txt', 'r')

lst = []
for state in range(int(input())):
    x, y = map(int, input().split())
    lst.append((x, y))

# for s in sorted(lst, key=lambda x:(x[0],x[1])):
#     print(*s)

for s in sorted(lst, key=lambda x:(x[1],x[0])):
    print(*s)