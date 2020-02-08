'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인
수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''
def perm(k, n):
    global M
    if k == M:
        print(*order)
        return

    for i in range(1, N+1):
        if visit[i]: continue
        order.append(i)
        perm(k+1, n)
        order.pop()

order = []
N, M = map(int, input().split())
visit = [0] * (N+1)
perm(0, N)