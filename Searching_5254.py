import sys; sys.stdin = open("txt/Searching_5254.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, word = input().split()
    N = int(N)

    word_list = set()
    cnt = 0
    for _ in range(len(word)):
        for i in range(len(word)+1):
            if cnt+i <= len(word):
                word_list.add(word[cnt:cnt+i])
        cnt += 1
    word_list = list(word_list)
    word_list.sort()
    print('#{} {} {}'.format(tc, word_list[N][0], len(word_list[N])))