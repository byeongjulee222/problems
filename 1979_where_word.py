import sys; sys.stdin = open("txt/1979_where_word.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [['0' for _ in range(N+2)]] + [['0'] + list(input().split()) + ['0'] for _ in range(N)] + [['0' for _ in range(N+2)]]

    cnt = 0
    for i in range(N+2):
        for j in range(N+2):
            word_x = word_y = ''
            for k in range(K+2):
                if j+k < N+2:
                    word_x += arr[i][j+k]
                    word_y += arr[j+k][i]
                    # print(word_x)
            if '0'+'1'*K+'0' == word_x:
                cnt += 1
            if '0'+'1'*K+'0' == word_y:
                cnt += 1

    print('#{} {}'.format(tc, cnt))