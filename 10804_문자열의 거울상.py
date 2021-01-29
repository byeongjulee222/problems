import sys; sys.stdin=open('txt/10804_문자열의 거울상.txt', 'r')

for tc in range(1, int(input())+1):
    word = input()
    ans = ''
    for w in reversed(word):
        if w == 'b':
            ans += 'd'
        elif w == 'd':
            ans += 'b'
        elif w == 'p':
            ans += 'q'
        else:
            ans += 'p'
    print('#{} {}'.format(tc, ans))