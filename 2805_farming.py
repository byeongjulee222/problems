import sys; sys.stdin = open("txt/2805_farming.txt", "r")

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)

    result = []
    for i in range(-N//2, N//2+1):
        for j in range(-N//2, N//2+1):
            if abs(i)+abs(j) <= N//2:
                result.append((i, j))
    # print(result)

    SUM = 0
    for area in result:
        SUM += arr[N//2 + area[0]][N//2 + area[1]]

    print('#{} {}'.format(tc, SUM))



# print(1+3+5+7+5+3+1)