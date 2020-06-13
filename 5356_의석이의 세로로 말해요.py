import sys; sys.stdin = open("txt/5356_speak_word.txt", "r")

T = int(input())
for tc in range(1, T+1):
# print(T)

    arr = [list(input()) for _ in range(5)]

    # print(arr)
    len_list = []
    for word in arr:
        len_list.append(len(word))

    # print(len_list)
    max_len = max(len_list)
    for word in arr:
        if len(word) < max_len:
            for _ in range(max_len-len(word)):
                word.append(' ')

    # print(arr)
    result = ''
    for j in range(max_len):
        for i in range(5):
            result += arr[i][j]
    print('#{} {}'.format(tc, result.replace(' ', '')))