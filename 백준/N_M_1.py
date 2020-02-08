'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인
수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''
def perm(k):
    global M
    if k == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if visit[i]: continue
        visit[i] = 1
        arr.append(i)
        perm(k+1)
        visit[i] = 0
        arr.pop()

arr = []
N, M = map(int, input().split())
visit = [0] * (N+1)
perm(0)