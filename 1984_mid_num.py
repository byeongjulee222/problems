import sys; sys.stdin = open("txt/1984_mid_num.txt", "r")

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    print('#{} {:.0f}'.format(tc, (sum(arr)-max(arr)-min(arr))/(len(arr)-2)))