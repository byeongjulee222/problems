import sys; sys.stdin = open('txt/1427_소트인사이드.txt', 'r')

num = list(map(int, input()))
for i in sorted(num, reverse=True):
    print(i, end='')
