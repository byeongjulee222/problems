import sys; sys.stdin = open("txt/Searching_5253.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = [input() for _ in range(N)]
    M_list = [input() for _ in range(M)]
    # print(N_list)
    cnt = 0
    for _ in range(len(M_list)):
        word = M_list.pop(0)
        for j in N_list:
            if word == j[:len(word)]:
                cnt += 1
                break
    print('#{} {}'.format(tc, cnt))