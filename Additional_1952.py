import sys; sys.stdin = open('txt/Additional_1952.txt', 'r')

def swim(n, Sum):
    global Min

    if Sum > Min:
        return

    if n >= 12:
        if Min > Sum:
            Min = Sum
        return

    swim(n+1, Sum + (arr[n]*cost[0]))
    swim(n+1, Sum + cost[1])
    swim(n+3, Sum + cost[2])

T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # print(arr)
    Min = cost[3]
    swim(0, 0)
    print('#{} {}'.format(tc, Min))