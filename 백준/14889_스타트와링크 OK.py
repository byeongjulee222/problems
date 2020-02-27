import sys; sys.stdin = open('txt/14889_스타트와링크.txt', 'r')
from itertools import combinations

for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    member = list(range(N))

    Min = 999999
    # 팀을 두 개로 나누기 (조합)
    for group1 in combinations(member, N // 2):
        group2 = list(set(member) - set(group1))

        # 1팀, 2팀 능력치 계산
        team_1, team_2 = 0, 0
        for i, j in combinations(group1, 2):
            team_1 += arr[i][j] + arr[j][i]
        for i, j in combinations(group2, 2):
            team_2 += arr[i][j] + arr[j][i]
        Min = min(Min, abs(team_1 - team_2))

    print(Min)

# 두 그룹으로 나누는 문제 코드 구현
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