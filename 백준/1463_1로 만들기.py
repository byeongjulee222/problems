import sys; sys.stdin=open('txt/1463_1로 만들기.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    ans = [0 for _ in range(N+1)]
    for i in range(2, N+1):
        candi = list()
        if not i % 3: candi.append(ans[i//3]+1)
        if not i % 2: candi.append(ans[i//2]+1)
        candi.append(ans[i-1]+1)

        ans[i] = min(candi)

    print(ans[N])
