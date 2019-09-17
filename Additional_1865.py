import sys; sys.stdin = open("txt/Additional_1865.txt", "r")

# def find(row):
#     global Max, result
#
#     # 원소값이 소수값이기 때문에 어떤수를 곱하더라도 작아짐
#     if Max >= result:
#         return
#
#     # 마지막 행에 도달했다면 계산이 끝난 것이기 때문에 최댓값 계산
#     if row == N:
#         Max = max(Max, result)
#         return
#
#     # 한 행씩 비교
#     for i in range(N):
#         # 방문한 곳이면 바로 끝(튕김)
#         if check[i]:
#             continue
#         # 원소값이 0이면 바로 끝(튕김)
#         if arr[row][i] == 0:
#             continue
#
#         check[i] = True
#         result *= arr[row][i]
#         print(arr[row][i])
#         print(result)
#         find(row+1)
#
#         check[i] = False
#         result /= arr[row][i]
#
#
#
# T = int(input())
# # for tc in range(1, T+1):
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         arr[i][j] /= 100
# check = [0] * N
# result = 1
# Max = 0
# find(0)
# print('{:.6f}'.format(Max*100))



def find(row):
    global Max, result

    if Max >= result:
        return
    if row == N:
        Max = max(Max, result)
        return

    for col in range(N):
        if check[col]:
            continue
        if arr[row][col] == 0:
            continue

        check[col] = True
        result *= arr[row][col]
        find(row + 1)
        check[col] = False
        result /= arr[row][col]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100

    check = [False] * N
    result = 1
    Max = 0
    find(0)
    print('#{} {:.6f}'.format(tc, Max*100))






