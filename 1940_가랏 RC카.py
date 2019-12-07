import sys; sys.stdin = open('txt/1940_가랏 RC카.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    res = 0
    now = 0
    arr = []
    for _ in range(N):
        arr.append(input())
        # print(arr[n][0])
    # print(arr)

    for n in arr:
        if n[0] == '1':
            now = now + int(n[2])
            res += now
        elif n[0] == '2':
            if now < int(n[2]): now = 0
            else:
                now = now - int(n[2])
                res += now
        else:
            res += now


    print('#{} {}'.format(tc, res))