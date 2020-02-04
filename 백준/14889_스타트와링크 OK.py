import sys; sys.stdin = open('txt/14889_스타트와링크.txt', 'r')
from itertools import combinations

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    member = list(range(N))
    set1 = list(combinations(member, N // 2))
    Min = 999999
    for group in set1:
        rest = list(set(member) - set(group))

        group_comb = list(combinations(group, 2))
        group_rest = list(combinations(rest, 2))

        A, B = 0, 0
        for (i, j) in group_comb:
            A += arr[i][j] + arr[j][i]
        for i, j in group_rest:
            B += arr[i][j] + arr[j][i]
        Min = min(Min, abs(A - B))
    #
    print(Min)

# 두 그룹으로 나누는 문제 코드 구현
'''
N = 4
# acnt, bcnt 를 index로 사용
def backtrack(k, acnt, bcnt):
    if acnt > N // 2 or bcnt > N // 2: return

    if acnt == N // 2 and bcnt == N // 2:
        print(A[:acnt], B[:acnt])
        return

    # k번 값을 A에 추가할지 B에 추가할지
    A[acnt] = k
    backtrack(k + 1, acnt + 1, bcnt)
    # B에 추가할지
    B[bcnt] = k
    backtrack(k + 1, acnt, bcnt + 1)


# 인덱스 저장
A = [0] * N
B = [0] * N

backtrack(1, 1, 0)
'''