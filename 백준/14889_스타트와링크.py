import sys; sys.stdin = open('txt/14889_스타트와링크.txt', 'r')
# 조합으로도 짤 수 있다.

# 부분집합
# SW아카데미 요리사 문제와 비슷
# 두 팀으로 나누는데 능력치 차이가 가장 작게
# A 팀 / B 팀 나눠서 A로 넣고 B로 넣고
# Min = abs(A-B)


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # break







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