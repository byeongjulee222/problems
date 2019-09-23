import sys; sys.stdin = open("txt/Additional_1486.txt")

def f(n, r, sum):
    global B
    if sum >= B:
        result.append(sum)
    if n == r:
        return
    f(n+1, r, sum + arr[n])
    f(n+1, r, sum)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    f(0, N, 0)
    print('#{} {}'.format(tc, min(result)-B))


# def backtrack(k, N, sum):
#     global Min
#     #답이면 원하는 작업을 한다
#     if k == N:
#         if sum >= B and Min > sum - B:
#             Min = sum - B
#         return
#
#     if sum >= Min + B:
#         return
#     k += 1
#     backtrack(k, N, sum + arr[k - 1])
#     backtrack(k, N, sum)
#
# TC = int(input())
# for tc in range(1, TC + 1):
#     N, B = map(int, input().split())
#     arr = list(map(int, input().split()))
#     Min = 10000 * N - B
#
#     backtrack(0, N, 0)
#     print('#{} {}'.format(tc, Min))