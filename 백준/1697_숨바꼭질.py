import sys; sys.stdin = open('txt/1697_숨바꼭질.txt', 'r')
from collections import deque

n, k = map(int, input().split())
Max = 100001
arr = [0 for _ in range(Max)]

def bfs():
    q = deque()
    q.append(n)
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            print(arr)
            return arr[now_pos]
        for next_pos in [now_pos - 1, now_pos + 1, now_pos * 2]:
            if 0 <= next_pos < Max and not arr[next_pos]:
                arr[next_pos] = arr[now_pos] + 1
                q.append(next_pos)

print(bfs())