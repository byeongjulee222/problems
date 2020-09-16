import sys; sys.stdin = open("txt/10845_큐.txt")
from collections import deque

N = int(sys.stdin.readline())

q = deque()
cnt = 0
for _ in range(N):
    word = sys.stdin.readline().split()
    if word[0] == 'push':
        q.append(word[1])
        cnt += 1
    elif word[0] == 'front':
        if q: print(q[0])
        else: print(-1)
    elif word[0] == 'back':
        if q: print(q[-1])
        else: print(-1)
    elif word[0] == 'size':
        print(cnt)
    elif word[0] == 'empty':
        if q: print(0)
        else: print(1)
    elif word[0] == 'pop':
        if q:
            print(q.popleft())
            cnt -= 1
        else: print(-1)