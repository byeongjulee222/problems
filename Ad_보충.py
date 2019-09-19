'''
순열 / 조합 생성 <--- 백트래킹 이해
순열 / 조합 생성하는 방법 -> 재귀 호출
        ---> 상태 공간 트리 --> 재귀 함수 호출 트리
        ---> 선택의 과정
재귀 함수 호출 트리
부분집합을 생성
원소의 수 = N
N 번의 선택을 통해 부분집합을 생성, 각 원소에 대해서
매번 선택할 때의 선택지 ==> 2개
'''
# k : 트리의 높이(index)
path = [0] * 3
def subset(k,n):
    global cnt
    if k == n:
        print(path)
        return
    # cnt += 1
    # 함수호출이 선택이다.
    path[k] = -1; subset(k + 1, n)
    path[k] = 1; subset(k + 1, n)

# cnt = 1
# print(cnt)
# subset(0, 3)

'''
순열 생성
모든 순열을 생성하는 과정을 선택하는 과정
'''
# cnt = 0
# N = 3 # (0, 1, 2) 요소에 대하여
# visit = [0] * 3
# for i in range(N):
#     visit[i] = 1
#     # ------ 패턴이 반복됨 -------#
#     for j in range(N):
#         if visit[j]: continue
#         visit[j] = 1
#         # ------ 패턴이 반복됨 -------#
#         for k in range(N):
#             if visit[k]: continue
#             visit[k] = 1
#             print(i, j, k)
#             visit[k] = 0
#         # ------ 패턴이 반복됨 -------#
#         visit[j] = 0
#     # ------ 패턴이 반복됨 -------#
#     visit[i] = 0


order = []
N = 3
visit = [0] * N
def perm(k, n):
    if k == n:
        print(order)
        return

    for i in range(N):
        if visit[i]: continue
        visit[i] = 1
        order.append(i)
        # print(order)
        perm(k+1, n)
        order.pop()
        # print(order)
        visit[i] = 0

perm(0, N)


'''
# 조합 생성
arr = 'ABCDE'
N = 5
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])
'''

'''
arr = 'ABCDE'
N, R = 5, 3
choose = []
def comb(k, s):
    if k == R:
        print(choose)
        return

    for i in range(s, N):
        choose.append(arr[i])
        comb(k+1, i+1)
        choose.pop()


comb(0, 0)
'''