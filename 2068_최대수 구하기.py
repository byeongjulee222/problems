import sys; sys.stdin = open("txt/2068.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    # Max = arr[0]
    # for num in arr:
    #     if num >= Max:
    #         Max = num
    print(max(arr))
    # print('#{} {}'.format(tc, Max))