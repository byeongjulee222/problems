import sys; sys.stdin = open('txt/SW_4008_숫자 만들기.txt', 'r')

def cal(res, cnt, plus, minus, mul, div):
    global Max, Min
    if cnt == N:
        Max = max(Max, res)
        Min = min(Min, res)

    if plus:
        cal(res+arr[cnt], cnt+1, plus-1, minus, mul, div)
    if minus:
        cal(res-arr[cnt], cnt+1, plus, minus-1, mul, div)
    if mul:
        cal(res*arr[cnt], cnt+1, plus, minus, mul-1, div)
    if div:
        cal(int(res/arr[cnt]), cnt+1, plus, minus, mul, div-1)


for tc in range(1, int(input())+1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    arr = list(map(int, input().split()))

    Max = -999999999
    Min = 999999999
    cal(arr[0], 1, plus, minus, mul, div)
    print(f'#{tc} {Max-Min}')