from sys import stdin
from collections import deque
N = int(stdin.readline())

lst = deque([i for i in range(1, N+1)])
# print(lst)
if len(lst) == 1: print(1)
elif len(lst) == 2: print(2)
else:
    while len(lst) > 1:
        lst.popleft()
        change = lst.popleft()
        lst.append(change)
        # print(lst)

    print(lst[0])