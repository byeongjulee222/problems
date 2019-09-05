import sys; sys.stdin = open("txt/1859_millionaire.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    MAX = max(arr)
    MIN = min(arr)
    buy = sell = 0
    buy_cnt = 0
    for i in range(len(arr)):
        if i == len(arr)-2:
            if arr[i] <= arr[i+1]:
                buy += arr[i]
                buy_cnt += 1
        elif i == len(arr)-1:
            if buy_cnt == 0:
                break
            else:
                sell += arr[i]*buy_cnt
        else:
            if arr[i] == MIN:
                buy += arr[i]
                buy_cnt += 1
            elif arr[i] == MAX:
                sell += arr[i]*buy_cnt
                buy_cnt = 0
            elif arr[i] == MAX:
                continue


    print('#{} {}'.format(tc, sell-buy))