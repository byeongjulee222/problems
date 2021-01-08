import sys; sys.stdin = open('txt/13305_주유소.txt', 'r')

for tc in range(int(input())):
    city_num = int(input())
    dist = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    ans = dist[0] * cost[0]

    # 현재까지 cost 중 가장 저렴한 것으로 넣는다 생각
    Min = cost[0]
    for i in range(1, city_num-1):
        if Min > cost[i]: Min = cost[i] # 이게 Min = min(Min, cost[i]) 보다 12ms 빠름
        ans += Min * dist[i]
    print(ans)