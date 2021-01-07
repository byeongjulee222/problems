import sys; sys.stdin = open('txt/11399_ATM.txt', 'r')

nums = int(input())
clients = sorted(list(map(int, input().split())))
##
ans = 0
length = len(clients)
for time in clients:
    ans += time * length
    length -= 1

print(ans)