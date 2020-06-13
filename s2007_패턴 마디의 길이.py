import sys; sys.stdin = open("txt/2007_pattern_len.txt", "r")

T = int(input())

for tc in range(1, T+1):
    word = input()
    # result = []
    for i in range(1, 11):
        if word[:i] == word[i:2*i]:
            print(word[:i])
            break
    # print('#{} {}'.format(tc, result[1]))