import sys; sys.stdin = open("txt/2805_farming.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     result = []
#     for i in range(-N//2, N//2+1):
#         for j in range(-N//2, N//2+1):
#             if abs(i)+abs(j) <= N//2:
#                 result.append((i, j))
#
#     SUM = 0
#     for area in result:
#         SUM += arr[N//2 + area[0]][N//2 + area[1]]
#
#     print('#{} {}'.format(tc, SUM))
#


#############################################################
for tc in range(int(input())):
    N = int(input())

    i = N // 2
    j = N // 2 + 1
    res = cnt = 0
    for _ in range(N):
        data = [list(input())]
        for k in range(i, j):
            res += int(data[0][k])
        if cnt < N // 2:
            i -= 1
            j += 1
            cnt += 1
            continue
        i += 1
        j -= 1
    print('#{} {}'.format(tc + 1, res))