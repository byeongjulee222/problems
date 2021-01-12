import sys; sys.stdin = open('txt/10814_나이순 정렬.txt', 'r')

# 3996ms
lst = []
for i in range(int(input())):
    a, b = input().split()
    lst.append((a, b, i))

for word in sorted(lst, key=lambda x:(int(x[0]), x[2])):
    print(word[0], word[1])


'''4876ms
lst = []
for _ in range(int(input())):
    lst.append(input().split())

for word in sorted(lst, key=lambda x:int(x[0])):
    print(*word)
'''