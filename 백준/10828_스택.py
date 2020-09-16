import sys; sys.stdin = open('txt/10828_스택.txt')

N = int(sys.stdin.readline())
lst = []
cnt = 0
for _ in range(N):
    word = sys.stdin.readline().split()
    if word[0] == 'push':
        lst.append(word[1])
        cnt += 1
    elif word[0] == 'top':
        if lst:
            print(lst[-1])
        else:
            print(-1)
    elif word[0] == 'size':
        print(cnt)
    elif word[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    elif word[0] == 'pop':
        if lst:
            print(lst.pop(-1))
            cnt -= 1
        else:
            print(-1)